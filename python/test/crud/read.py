from test.engine import session;
from test.schema.sku import Sku as sku;
from test.test_sku import Sku;
from sqlalchemy import select;

def show():
    with session() as db_s:
        first_record = db_s.query(Sku).all();

        res = [sku.from_orm(i) for i in first_record];
    return res;
