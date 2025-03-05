import os
from fastapi import FastAPI 
from routers import producto, producto_db, usuario
from db import model, database
from db.database import engine

app = FastAPI()

# CREA LAS TABLAS Y EJECUTA EL "import.sql" SÓLO SI NO EXISTE EL ARCHIVO "database.db"
def initialize_db():
    if not os.path.exists('db/database.db'):
        print("Cargando datos...")
        model.Base.metadata.create_all(bind=engine)
        database.run_import_sql()
    else:
        print("Cargando datos...")


initialize_db() 

app.include_router(producto.router)
app.include_router(producto_db.router)
app.include_router(usuario.router)
