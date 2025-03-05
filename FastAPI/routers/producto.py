from typing import Optional
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from routers.usuario import oauth2_scheme

router = APIRouter(
    prefix="/producto", 
    tags=["producto"], 
    responses={404: {"message": "No se han encontrado productos"}}
)

class Producto(BaseModel):
    id: Optional[int] = None
    nombre: str
    precio: float
    descripcion: Optional[str] = None
    oferta: bool

lista_productos = [
    Producto(id=1, nombre="Laptop", precio=1200.00, descripcion="Laptop Lenovo", oferta=False),
    Producto(id=2, nombre="Mouse", precio=20.00, descripcion="Mouse inalámbrico", oferta=True),
    Producto(id=3, nombre="Teclado", precio=30.00, descripcion="Teclado mecánico", oferta=False),
]

ultimo_id = 3

@router.get("/")
async def get_productos():
    return lista_productos

@router.get("/{producto_id}")
async def get_producto(producto_id: int):
    producto = find_by_id(producto_id)
    return producto

@router.post("/", status_code=201)
async def create_producto(producto: Producto): 
    global ultimo_id
    
    if any(p.nombre == producto.nombre for p in lista_productos):
        raise HTTPException(status_code=409, detail="Ya existe un producto con el mismo nombre")
    
    for p in lista_productos:
        if p.id > ultimo_id:
            ultimo_id = p.id
    
    ultimo_id += 1
    producto.id = ultimo_id
    lista_productos.append(producto)
    
    return producto


@router.put("/{id}", status_code=200)
async def update_producto(id: int, producto: Producto):
    producto_en_lista = find_by_id(id)
    producto_en_lista.nombre = producto.nombre
    producto_en_lista.descripcion = producto.descripcion
    producto_en_lista.precio = producto.precio
    producto_en_lista.en_oferta = producto.en_oferta
    return producto_en_lista

@router.delete("/{id}", status_code=204)
async def delete_producto(id: int):
    producto = find_by_id(id)
    lista_productos.remove(producto)
    

# -------------------------------------------------------------------------------------------------------------

def find_by_id(id: int):
    for producto in lista_productos:
        if producto.id == id:
            return producto
    raise HTTPException(status_code=404, detail=f"No se ha encontrado ningún producto con ID: {id}")