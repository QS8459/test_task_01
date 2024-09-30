from src.db.engine import session;
from src.schema.sku import Sku as sku;
from src.db.model.sku import Sku;
from sqlalchemy import select;

def show():
    with session() as db_s:
        first_record = db_s.query(Sku).all();

        res = [sku.from_orm(i) for i in first_record];
    return res;
