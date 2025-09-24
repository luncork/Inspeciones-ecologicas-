from fastapi import FastAPI

app = FastAPI()

# Endpoint de prueba
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de inspecciones ecológicas"}
