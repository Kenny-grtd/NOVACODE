from datetime import datetime, timezone

from sqlmodel import Field, SQLModel

from app.models.enums import Rol


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"

    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    password_hash: str
    rol: str = Field(default=Rol.CIUDADANO.value, index=True)
    is_active: bool = True
    created_at: datetime = Field(default_factory=utcnow)

    # Datos del registro ampliado (heredados de la versión 1)
    tipo_identificacion: str | None = None
    numero_identificacion: str | None = Field(default=None, index=True)
    nombres: str | None = None
    apellidos: str | None = None
    genero: str | None = None
    direccion: str | None = None
    telefono: str | None = None
    departamento: str | None = None
    ciudad: str | None = None
    etnia: str | None = None
    persona_vulnerable: str | None = None
