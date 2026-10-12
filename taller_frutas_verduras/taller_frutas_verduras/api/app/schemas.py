from pydantic import BaseModel

class ProductoBase(BaseModel):
    sku: str
    nombre: str
    tipo: str
    precio: int
    unidad: str

    class Config:
        from_attributes = True
