import os

from dotenv import load_dotenv
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
connection = f"mysql+pymysql://{os.getenv('USER_DB_ENCUESTA')}:{os.getenv('PASS_DB_ENCUESTA')}@{os.getenv('IP_DB_ENCUESTA')}:{os.getenv('PORT_DB_ENCUESTA')}/{os.getenv('NAME_DB_ENCUESTA')}"
engine = create_engine(connection)
SessionLocal = sessionmaker(autoflush=False, autocommit =False, bind=engine)
Base = declarative_base()
meta = MetaData()