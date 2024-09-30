from test.engine import session;
from test.test_sku import Sku;

def write(item):

    try:
        with session() as db_s:
            sku = Sku(**item);
            db_s.add(sku);
            db_s.commit();
    except Exception as e:
        raise e;

