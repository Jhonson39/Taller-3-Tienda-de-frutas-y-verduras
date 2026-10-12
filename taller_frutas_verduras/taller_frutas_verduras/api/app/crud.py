from sqlalchemy.orm import Session
from .models import Producto

def obtener_productos(db: Session, tipo: str | None = None):
    consulta = db.query(Producto)
    if tipo:
        consulta = consulta.filter(Producto.tipo.ilike(tipo))
    return consulta.order_by(Producto.nombre).all()

def obtener_producto_por_sku(db: Session, sku: str):
    return db.query(Producto).filter(Producto.sku == sku).first()
