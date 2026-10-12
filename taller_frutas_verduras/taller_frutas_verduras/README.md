# Taller 3: Tienda virtual de frutas y verduras

Proyecto sencillo para practicar Docker Compose con tres servicios:
- **web**: página web hecha con Flask.
- **api**: API hecha con FastAPI.
- **database**: base de datos PostgreSQL.

La tienda muestra frutas y verduras de ejemplo. El código está escrito de forma sencilla para alguien que está empezando.

## Requisitos
Tener Docker Desktop instalado y funcionando.

## Cómo ejecutar
1. Descomprime el archivo ZIP.
2. Abre una terminal dentro de la carpeta `taller_frutas_verduras`.
3. Copia el archivo de ejemplo de variables:
   ```bash
   cp .env.example .env
   ```
   En Windows PowerShell puedes copiarlo con:
   ```powershell
   Copy-Item .env.example .env
   ```
4. Inicia los contenedores:
   ```bash
   docker compose up --build
   ```
5. En otra terminal, carga los productos de ejemplo:
   ```bash
   docker compose exec api python -m app.seed
   ```
6. Abre la tienda en http://localhost:5000
7. Para revisar la API, abre http://localhost:8000/docs

## Comandos útiles
- Ver contenedores: `docker compose ps`
- Ver mensajes de la API: `docker compose logs -f api`
- Detener todo: `docker compose down`
- Detener y borrar también los datos guardados: `docker compose down -v`

## ¿Cómo se comunican?
La página web (`web`) le pide los productos a la API (`api`) usando HTTP. La API consulta PostgreSQL (`database`). Dentro de Docker se usan los nombres `api` y `database`, no `localhost`.

## Nota
Es un proyecto educativo. Los precios y productos son inventados para hacer pruebas.
