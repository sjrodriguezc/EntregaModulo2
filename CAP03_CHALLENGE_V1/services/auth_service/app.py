from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic_settings import BaseSettings
from services.auth_service.routes import router as auth_router

class Settings(BaseSettings):
    jwt_secret: str = "supersecret"
    jwt_algorithm: str = "HS256"
    class Config:
        env_file = ".env"

settings = Settings()

app = FastAPI(
    title="Auth Service",
    description="Servicio de autenticación y gestión de usuarios.",
    version="1.0.0",
    openapi_tags=[
        {"name": "auth", "description": "Operaciones de autenticación"}
    ]
)

app.include_router(auth_router)  # <--- SIN prefix

@app.get("/", tags=["root"])
def read_root():
    return {"message": "Welcome to the Auth Service"}

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Error interno del servidor", "error": str(exc)},
    )