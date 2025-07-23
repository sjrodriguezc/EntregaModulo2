from fastapi import FastAPI
from services.user_profile_service.routes import router as user_profile_router  # Importa el router correctamente

app = FastAPI(title="User Profile Service")

# Incluye el router en la app bajo el prefijo /user_profiles para mantener ordenadas las rutas
app.include_router(user_profile_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the User Profile Service"}