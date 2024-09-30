from sqlalchemy import create_engine, MetaData;
from sqlalchemy.orm import sessionmaker;
from contextlib import contextmanager;
from src.config import settings;
import typing

engine=create_engine(str(settings.pg_uri));
metadata = MetaData();
Session = sessionmaker(bind=engine);

@contextmanager
def session() -> typing.ContextManager[Session]:
	session = Session()
	try:
		yield session;
		session.commit();
	except:
		session.rollback();
		raise;
	finally:
		session.close();
