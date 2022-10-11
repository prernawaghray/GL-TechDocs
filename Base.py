from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import yaml

with open('database_config.yml') as stream:
    configs = yaml.safe_load(stream)

def get_connection():
    return create_engine(url=configs['SQLALCHEMY_DATABASE_URI'])

def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()

# Create a new session
engine = get_connection()
_SessionFactory = sessionmaker(bind=engine)
Base = declarative_base()

