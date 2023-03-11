from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('postgresql://crhsaqci:i9MqAfGgWHpj530fj5_GQWyHyTrZ-YeI@mouse.db.elephantsql.com:5432/crhsaqci')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
