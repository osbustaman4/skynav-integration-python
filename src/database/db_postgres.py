from decouple import config as config_environment

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

Base = declarative_base()

POSTGRES_HOST = config_environment('POSTGRES_HOST')
POSTGRES_USER = config_environment('POSTGRES_USER')
POSTGRES_PASSWORD = config_environment('POSTGRES_PASSWORD')
POSTGRES_PORT = config_environment('POSTGRES_PORT')
POSTGRES_DB = config_environment('POSTGRES_DB')

encoded_password = quote_plus(POSTGRES_PASSWORD)

connection_string = f"postgresql://{POSTGRES_USER}:{encoded_password}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
engine = create_engine(connection_string)

Session = sessionmaker(bind=engine)