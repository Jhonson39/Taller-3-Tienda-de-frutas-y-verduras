from sqlalchemy import Column, Integer, String
from .database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True, index=True, nullable=False)
    nombre = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    precio = Column(Integer, nullable=False)
    unidad = Column(String, nullable=False)
