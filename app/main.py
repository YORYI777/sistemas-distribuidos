from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def root():
    return {
        "mensaje": "Sistema Distribuido funcionando",
        "hostname": socket.gethostname()
    }
