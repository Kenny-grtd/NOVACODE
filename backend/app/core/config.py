from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuración de la app. Se lee de variables de entorno / archivo .env."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "NOVACODE PQRS"
    database_url: str = "sqlite:///./novacode.db"

    secret_key: str = "cambia-esto-en-produccion"
    access_token_expire_minutes: int = 60

    email_sender: str = ""
    email_password: str = ""
    smtp_server: str = "smtp.gmail.com"
    smtp_port: int = 587
    empresa_nombre: str = "NOVACODE"

    # Orígenes permitidos para CORS (separados por coma). Solo se necesita cuando
    # el frontend se abre fuera de Docker (p. ej. Live Server en el puerto 5500).
    cors_origins: str = "http://localhost:3000,http://localhost:5500,http://127.0.0.1:5500"

    @property
    def cors_origin_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]


settings = Settings()
