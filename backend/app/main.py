from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers import health
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="API de la plataforma NOVACODE para la gestión de PQRS.",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)

# TODO: registrar aquí los routers de auth, pqrs, usuarios y reportes.
