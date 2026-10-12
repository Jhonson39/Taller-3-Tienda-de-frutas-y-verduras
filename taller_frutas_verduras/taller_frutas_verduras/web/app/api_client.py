import requests
from config import API_URL

def obtener_productos(tipo=None):
    try:
        parametros = {}
        if tipo:
            parametros["tipo"] = tipo
        respuesta = requests.get(f"{API_URL}/productos/", params=parametros, timeout=4)
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.RequestException:
        return []

def obtener_producto(sku):
    try:
        respuesta = requests.get(f"{API_URL}/productos/{sku}", timeout=4)
        if respuesta.status_code == 404:
            return None
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.RequestException:
        return None
