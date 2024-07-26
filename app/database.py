from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg
from psycopg.rows import dict_row
import time

from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True: 
#     try:
#         conn = psycopg.connect(host='localhost', dbname='fastAPI',
#                                user='postgres', password='#Just2024', row_factory=dict_row)
        
#         cur = conn.cursor()
#         # Immediately test the connection
#         cur.execute('SELECT 1')
#         print("Database connection established successfully")
#         break
#     except Exception as e:
#         print("Unable to connect to the database")
#         print("Error:", e)
#         time.sleep(3)