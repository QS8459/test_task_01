from elasticsearch import Elasticsearch, helpers
from elasticsearch.exceptions import ConnectionError, NotFoundError;
from src.config import settings
es = Elasticsearch(
     hosts = [settings.es],
#     hosts = ["http://test_task_01-elasticsearch-run-25c90bae95fe:9200"],
     timeout =30
)
#Function to build a large list of items to insert into the elasticsearch sku_index 
def prepare_bulk(sku_data):
	bulk_actions:list = [];
	for row in sku_data:
		action = {
				"_index":"test_sku_index",
				"_id":row.uuid,
				"_source": {
					"_title":row.title,
					"_description":row.description,
					"_category_id":row.category_id,
					"_price_before_discounts":row.price_before_discounts
				}
			}
		bulk_actions.append(action);
	return bulk_actions;

#Actual insert function
def bulk_insert_sku_to_es(sku_data):
	bulk_actions = prepare_bulk(sku_data);
	helpers.bulk(es, bulk_actions);
	print(f'{len(bulk_actions)} records inserted into Es')

#Verification function to verify if data was inserted
def verify_data_inserted(uuid):
	try:
		result = es.get(index='test_sku_index', id = uuid)
		print("Elastic Search");
		print(result);
	except Exception as e:
		print(f"Error verifying data: {e}");

#Similar sku finder
def find_similar_products_custom(product_id, index='test_sku_index', size=5):
    try:
        
        product = es.get(index=index, id=product_id)
        product_data = product['_source']
        
        
        response = es.search(
            index=index,
            body={
                "query": {
                    "more_like_this": {
                        "fields": ["_title","_description"],
                        "like": [
                           {
                               "_id":product_id,
#                               "doc":product_data
                           }
                         ],
                        "min_term_freq":1,
                        "max_query_terms": 25
                    }
                },
                "size": size
            }
        )
        
        similar_products = response['hits']['hits'];
        tmp:dict = {'origin':product_id,'similar_uuids':[]};
        
        lst = [product['_id'] for product in similar_products]
        tmp.update({'similar_uuids':lst});
        return tmp
    except Exception as e:
        print(f"Error finding similar products: {e}")

#There is too much to write I guess I weather wirte explination and spend a little more time on this or rather I do tests and deploy my solution



def truncate_index(index_name:str="test_sku_index"):
	try:
		response = es.delete_by_query(
			index=index_name,
			body = {
				"query":{
					"match_all":{}
					}
				}
			)
		print(f"Deleted {response['deleted']} documents from index '{index_name}'");
	except Exception as e:
		print(f"Error deleting documnets: {e}");
