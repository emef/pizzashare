from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pizzashare import settings

engine = create_engine(settings.DB_ENGINE, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
