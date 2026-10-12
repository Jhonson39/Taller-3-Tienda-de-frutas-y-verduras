from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from . import crud, schemas

Base.metadata.create_all(bind=engine)
app = FastAPI(title="API de frutas y verduras")

@app.get("/")
def inicio():
    return {"mensaje": "API de frutas y verduras funcionando"}

@app.get("/productos/", response_model=list[schemas.ProductoBase])
def listar_productos(tipo: str | None = None, db: Session = Depends(get_db)):
    return crud.obtener_productos(db, tipo)

@app.get("/productos/{sku}", response_model=schemas.ProductoBase)
def detalle_producto(sku: str, db: Session = Depends(get_db)):
    producto = crud.obtener_producto_por_sku(db, sku)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto
