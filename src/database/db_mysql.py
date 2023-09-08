from decouple import config as config_environment

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

Base = declarative_base()

HOST = config_environment('HOST')
USER = config_environment('USER')
PASSWORD = config_environment('PASSWORD')
PORT = config_environment('PORT')
DB = config_environment('DB') 

encoded_password = quote_plus(PASSWORD)
connection_string = f"mysql://{USER}:{encoded_password}@{HOST}:{PORT}/{DB}"
engine = create_engine(connection_string, pool_pre_ping=True)
Session = sessionmaker(bind=engine)

