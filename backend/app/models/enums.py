from enum import Enum


class Rol(str, Enum):
    CIUDADANO = "ciudadano"
    FUNCIONARIO = "funcionario"
    ADMINISTRADOR = "administrador"


class TipoSolicitud(str, Enum):
    PETICION = "peticion"
    QUEJA = "queja"
    RECLAMO = "reclamo"
    SUGERENCIA = "sugerencia"


class EstadoSolicitud(str, Enum):
    # Propuesta inicial: ajustar con los estados que usaba la versión 1.
    RADICADA = "radicada"
    ASIGNADA = "asignada"
    EN_PROCESO = "en_proceso"
    RESPONDIDA = "respondida"
    CERRADA = "cerrada"
