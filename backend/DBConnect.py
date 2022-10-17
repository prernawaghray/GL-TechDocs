from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import yaml

with open('config.yaml') as stream:
    configs = yaml.safe_load(stream)

def get_connection():
    return create_engine(url=configs['DB_URL'])

def session_factory():
    Base.metadata.create_all(engine)
    return SessionFactory()

# Create a new session
engine         = get_connection()
SessionFactory = sessionmaker(bind=engine)
Base           = declarative_base()

