import sys;
import json;
from src.db.engine import session;
from sqlalchemy import select;
from src.db.model.sku import Sku;

def retrieve(uuid):
	with session() as db_s:
		quer = db_s.query(Sku).filter(Sku.uuid == uuid).all();
	return quer;



if __name__== "__main__":
	with session() as db_s:
		quer = db_s.query(Sku).filter(Sku.similar_sku is not None).limit(5).offset(0).all();
		#result = db_s.execute(quer).fetchall();
	res_dict:list = []
	for item in quer:
		print(item.uuid);
		tmp_d:dict = {};
		tmp_d = {
			"uuid":f'{item.uuid}',
			"product_id":item.product_id,
			"title":item.title,
			"similar_sku":f"""{[{
					'uuid': j.uuid,
					'title':j.title
					} for j in retrieve(item.similar_sku[0])]}"""
		}
		res_dict.append(tmp_d);
	#print(res_dict);
	with open(f"{sys.path[0]}/similar.json", 'w', encoding = 'utf-8') as file:
		
		json.dump(res_dict,file,ensure_ascii=False,indent=4);
