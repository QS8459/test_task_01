from test.parser.utils import find_cat
from test.crud.writer import write;
from lxml import etree;
import sys;
def reader(file_path):
    #Define a list to append all categories in order to build hierarchy
    cat_list:list = [];

    #Open whole file in binary format  
    with open(f"{sys.path[0]}/test/{file_path}", 'rb') as file:

         #Start for loop to parse all the categories 
         for event, element in etree.iterparse(file, events = ('end',), tag = 'category'):

            #Append all parsed category names, id and parentIds (if category has one)
            cat_list.append({'name':element.text, 'id':int(element.get('id')), 'parentId': int(element.get('parentId')) if element.get('parentId') is not None else None})

            #Clear out the 'element' cause the 'offer' tag out of 'category' tag
            element.clear()


            #Move the read cursor to the beginning of the file 
         file.seek(0)

        #Start for loop to parse all the data about products 
         for event, element in etree.iterparse(file, events=('end',), tag = 'offer'):

            #Get the products category id of a product to build the hierarchy of categories
            cat_id = int(element.findtext('categoryId',90401))

            #Call the category hierarchy finder fiunction from the src/parser/utils.py module
            cat_lvl = find_cat(cat_list, cat_id)

            #Build the dict(json) format of parameters
            params = element.findall('param')
            features = {}
            if len(params) > 0:
                for item in params:
                    features[item.get('name')] = item.text

            #Scrape all the data with if cases in order to prevent None type error can't use try: except cause will have to repeat the code (i guess)
            items ={
                'product_id': int(element.get('id')),
                'category_id': int(element.findtext('categoryId', 0)),
                'description': element.findtext('description', ''),
                'brand': element.findtext('vendor', ''),
                'barcode': int(element.findtext('barcode',0)),
                'title': element.findtext('name',''),
                'seller_name': element.findtext('vendor',''),
                'price_before_discounts': int(element.findtext('oldprice',element.findtext('price',1))),
                'price_after_discounts':int(element.findtext('price',0)),
                'discount':float(element.findtext('price',0))/float(element.findtext('oldprice',element.findtext('price',1))) if element.find('oldprice') is not None else 0.0,
                'currency':element.findtext('currencyId',''),
                'first_image_url': element.findtext('picture',''),
                'category_lvl_1':cat_lvl.get('lvl1'),
                'category_lvl_2':cat_lvl.get('lvl2'),
                'category_lvl_3':cat_lvl.get('lvl3'),
                'category_remaining':cat_lvl.get('lvlr'),
                'features': features
            }
	    #Call the write function to write all scraped data into Postgres public.sku table; (Not the besgt practice I guess);
            write(items);
