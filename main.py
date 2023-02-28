"""
Ejercicio:
Fecha:
Comando relevantes terminal
> conda activate fast-api
> uvicorn main:app --reload
> conda install requests  -n fast-api
nota: (Ctrl+Shift+P), then select the Python: Select Interpreter.  En este caso Python  + Entorno fast-api
"""
from fastapi import FastAPI
from dotenv import load_dotenv
from routes.auth import auth_routes
from routes.users_github import users_github

app=FastAPI()
app.include_router(auth_routes,prefix="/api")
app.include_router(users_github, prefix="/api")

load_dotenv()