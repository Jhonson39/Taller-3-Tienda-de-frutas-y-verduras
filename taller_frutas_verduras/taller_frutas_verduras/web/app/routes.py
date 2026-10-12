from flask import Blueprint, render_template, request, abort
from . import api_client

rutas = Blueprint("rutas", __name__)

@rutas.route("/")
def inicio():
    tipo = request.args.get("tipo")
    productos = api_client.obtener_productos(tipo)
    return render_template("index.html", productos=productos, tipo=tipo)

@rutas.route("/producto/<sku>")
def detalle(sku):
    producto = api_client.obtener_producto(sku)
    if producto is None:
        abort(404)
    return render_template("detalle.html", producto=producto)

@rutas.app_errorhandler(404)
def no_encontrado(error):
    return render_template("404.html"), 404
