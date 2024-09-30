import typing
from sqlalchemy import create_engine, MetaData;
from contextlib import contextmanager;
from sqlalchemy.orm import sessionmaker;
from src.config import settings
engine = create_engine(settings.pg_uri)
metadata = MetaData();
Session = sessionmaker(bind=engine);

@contextmanager
def session() ->typing.ContextManager[Session]:
    session = Session();
    try:
        yield session;
    except Exception:
        session.rollback();
        raise;
    finally:
        session .close()
