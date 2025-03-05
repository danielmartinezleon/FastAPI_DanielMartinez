from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.model import Producto_tabla
from routers.producto import Producto
from routers.usuario import oauth2_scheme

router = APIRouter(
    prefix="/productoDB",
    tags=["productos_db"],
)

# DTO para la respuesta
class ProductoDto(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: float
    oferta: bool

    class Config:
        orm_mode = True

# Dependencia para la sesión de base de datos
def obtener_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependencia = Annotated[Session, Depends(obtener_db)]

# Endpoints

@router.get("/", response_model=List[ProductoDto])
async def listar_productos(db: db_dependencia):
    return db.query(Producto_tabla).all()

@router.get("/{producto_id}", response_model=ProductoDto)
async def obtener_producto(producto_id: int, db: db_dependencia):
    producto = db.query(Producto_tabla).filter(Producto_tabla.id == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/", status_code=201, response_model=ProductoDto)
async def crear_producto(datos_producto: Producto, db: db_dependencia, token: str = Depends(oauth2_scheme)):
    if db.query(Producto_tabla).filter(Producto_tabla.nombre == datos_producto.nombre).first():
        raise HTTPException(status_code=409, detail="El producto ya existe")
    
    nuevo_producto = Producto_tabla(
        nombre=datos_producto.nombre,
        descripcion=datos_producto.descripcion,
        precio=datos_producto.precio,
        oferta=datos_producto.oferta
    )
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

@router.put("/{producto_id}", status_code=200, response_model=ProductoDto)
async def actualizar_producto(producto_id: int, datos_producto: Producto, db: db_dependencia, token: str = Depends(oauth2_scheme)):
    producto_db = db.query(Producto_tabla).filter(Producto_tabla.id == producto_id).first()
    if not producto_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    producto_db.nombre = datos_producto.nombre
    producto_db.descripcion = datos_producto.descripcion
    producto_db.precio = datos_producto.precio
    producto_db.oferta = datos_producto.oferta
    
    db.commit()
    db.refresh(producto_db)
    return producto_db

@router.delete("/{producto_id}", status_code=204)
async def eliminar_producto(producto_id: int, db: db_dependencia, token: str = Depends(oauth2_scheme)):
    producto = db.query(Producto_tabla).filter(Producto_tabla.id == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    db.delete(producto)
    db.commit()
    
    return {"mensaje": "Producto eliminado"}
