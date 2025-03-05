from sqlalchemy import Column, Integer, String, Float, Boolean
from db.database import Base

class Producto_tabla(Base):
    __tablename__ = "producto"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, unique=True, nullable=False)
    descripcion = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    oferta = Column(Boolean, default=False)

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)