"""Base model for ValueCell Server"""

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # it can only be defined once in the whole project

#Alternatively, if using SQLAlchemy 2.0 style:
# from sqlalchemy.orm import DeclarativeBase

