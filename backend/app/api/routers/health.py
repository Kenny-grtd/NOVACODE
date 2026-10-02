from fastapi import APIRouter, Depends
from sqlmodel import Session, text

from app.core.database import get_session

router = APIRouter(tags=["Sistema"])


@router.get("/health", summary="Estado del servicio")
def health() -> dict:
    return {"status": "ok"}


@router.get("/health/db", summary="Estado de la conexión a la base de datos")
def health_db(session: Session = Depends(get_session)) -> dict:
    session.exec(text("SELECT 1"))
    return {"status": "ok", "database": "connected"}
