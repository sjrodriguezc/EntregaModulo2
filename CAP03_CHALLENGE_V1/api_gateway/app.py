from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router as api_router

app = FastAPI(
    title="API Gateway - Sistema de Reservas de Salas",
    description="Este servicio actúa como punto central para acceder a los distintos microservicios del sistema de reservas.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"mensaje": "¡Bienvenido al API Gateway del Sistema de Reservas de Habitaciones!"}