import json
from pathlib import Path
from .database import Base, engine, SessionLocal
from .models import Producto

Base.metadata.create_all(bind=engine)
archivo = Path(__file__).resolve().parent.parent / "data" / "productos.json"

with open(archivo, "r", encoding="utf-8") as f:
    productos = json.load(f)

db = SessionLocal()
try:
    for dato in productos:
        existe = db.query(Producto).filter(Producto.sku == dato["sku"]).first()
        if not existe:
            db.add(Producto(**dato))
    db.commit()
    print("Productos de ejemplo cargados correctamente.")
finally:
    db.close()
