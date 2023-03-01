# Python_Token_FastApi
Ejercicio con Python para generar Token con FastAPI
- Visual Code con Python
- Postman App, no web.  La comunicacion con la api es localhost

> Ejercicio del canal de youtube @NelsonCode, del ejercicio JSON Web Token , REST API con FastAPI.
> Video: https://www.youtube.com/watch?v=Of1V5JV6voc&t=907s

## Comando relevantes para trabajar con Visual Code & terminal
1. Anaconda, activar entorno virtual fast-api
```sh
conda activate fast-api
```
2. Servidor web uvicorn, ejecutar python principal
```sh
uvicorn main:app --reload
```
3. Instalar fastapi en Conda y su entorno virtual fast-api. Ejecutar una terminal
```sh
conda install -c conda-forge fastapi --name fast-api
```
4. Instalar python-dotenv en Conda y su entorno virtual fast-api. Ejecutar una terminal
```sh
conda install python-dotenv -n fast-api
```
5. Instalar request en Conda y su entorno virtual fast-api. Ejecutar una terminal
```sh
conda install requests  -n fast-api
```
6. Instalar pydantic en Conda y su entorno virtual fast-api. Ejecutar una terminal
```sh
conda install pydantic  -n fast-api
```
7. Instalar pyjwt en Conda y su entorno virtual fast-api. Ejecutar una terminal
```sh
conda install pyjwt -n fast-api
```

### Configurar el Select Interpreter, en Visual Studio
- Nota: Visual Code (Ctrl+Shift+P), then select the Python: Select Interpreter.  En este caso Python  + Entorno fast-api
