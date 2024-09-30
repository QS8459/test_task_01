import os;
import json
import sys;
from src.parser.parse import reader;
from elasticsearch import Elasticsearch
from src.crud.read import show;
from src.es import prepare_bulk ,bulk_insert_sku_to_es, verify_data_inserted, find_similar_products_custom;
from pydantic.types import UUID;
from src.crud.update import update_sku;
if __name__== "__main__":
    print("Started Main function");     
    #You can pass file name as an arugment to the main.py function 
    file_path = sys.argv[1];

    #Reader function scrapes all the data from the xml file you can chech the function from the src/parser/parse.py
    reader(file_path);
    
    #The show function get all the records from the psql.sku table in the postgres container
    a = show();

    #The bulk insert function inserts data from psql.sku table into the elasticsearch sku doc
    bulk_insert_sku_to_es(a);

    #The following cycle passes uuid of each and every file into the elasticsearch sku doc and seeks for most similar products 
    for item in a:
	
	#Returns list of uuid of the product that are similar to passed uuid
        data = find_similar_products_custom(item.uuid);
	#The return is a dict with the {'original': item.uuid, "similar_uuids":[list of uuid of similar porduct]
        #Updates particular item in table 
	update_sku(data);
