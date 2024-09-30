from sqlalchemy import update;
from test.engine import session;
from test.test_sku import Sku;


def update_sku(data):
	print(data)
	with session() as db_s:
		db_s.execute(
			update(Sku)
			.where(Sku.uuid == data.get('origin'))
			.values(similar_sku=data.get('similar_uuids'))
			)
		db_s.commit();
