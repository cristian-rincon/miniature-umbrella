import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base



SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sql_app.db")
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db:5432/myappdb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

