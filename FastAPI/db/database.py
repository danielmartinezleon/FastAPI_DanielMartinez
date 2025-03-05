from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


DATABASE_URL = "sqlite:///./db/database.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def run_import_sql():
    sql_file = "./db/import.sql" 
    if os.path.exists(sql_file):
        with engine.connect() as connection:
            with open(sql_file, "r", encoding="utf-8") as file:
                sql_script = file.read()
                connection.execute(text(sql_script))
            connection.commit()
        print("El archivo import.sql se ha ejecutado correctamente.")