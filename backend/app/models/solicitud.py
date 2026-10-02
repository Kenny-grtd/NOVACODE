from datetime import datetime

from sqlmodel import Field, SQLModel

from app.models.enums import EstadoSolicitud
from app.models.usuario import utcnow


class Solicitud(SQLModel, table=True):
    __tablename__ = "solicitud"

    id: int | None = Field(default=None, primary_key=True)
    radicado: str = Field(unique=True, index=True)
    tipo_solicitud: str = Field(index=True)
    asunto: str
    descripcion: str
    ubicacion: str | None = None
    area_responsable: str | None = Field(default=None, index=True)
    persona_vulnerable: str | None = None
    estado: str = Field(default=EstadoSolicitud.RADICADA.value, index=True)
    respuesta: str | None = None

    fecha_radicacion: datetime = Field(default_factory=utcnow)
    fecha_limite: datetime | None = None  # según plazo legal en días hábiles
    fecha_respuesta: datetime | None = None

    usuario_id: int = Field(foreign_key="usuario.id", index=True)  # ciudadano
    funcionario_id: int | None = Field(default=None, foreign_key="usuario.id")


class Adjunto(SQLModel, table=True):
    __tablename__ = "adjunto"

    id: int | None = Field(default=None, primary_key=True)
    solicitud_id: int = Field(foreign_key="solicitud.id", index=True)
    nombre_original: str
    ruta: str  # nombre guardado en disco (nunca expuesto públicamente)
    content_type: str | None = None
    tamano_bytes: int = 0
    es_respuesta: bool = False  # True si lo adjunta el funcionario
    created_at: datetime = Field(default_factory=utcnow)


class EstadoCambio(SQLModel, table=True):
    """Historial de trazabilidad. Solo se inserta, nunca se edita ni se borra."""

    __tablename__ = "estado_cambio"

    id: int | None = Field(default=None, primary_key=True)
    solicitud_id: int = Field(foreign_key="solicitud.id", index=True)
    estado_anterior: str | None = None
    estado_nuevo: str
    observacion: str | None = None
    usuario_id: int | None = Field(default=None, foreign_key="usuario.id")
    fecha_cambio: datetime = Field(default_factory=utcnow)
