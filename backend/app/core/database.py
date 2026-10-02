from collections.abc import Generator

from sqlmodel import Session, create_engine

from app.core.config import settings

_connect_args = (
    {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}
)
engine = create_engine(
    settings.database_url, pool_pre_ping=True, connect_args=_connect_args
)


def get_session() -> Generator[Session, None, None]:
    """Dependencia de FastAPI: una sesión de BD por petición."""
    with Session(engine) as session:
        yield session
