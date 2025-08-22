# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENV: str = "production"
    # Si está definida, se usa (p.ej. Postgres). Si no, caemos a SQLite.
    DATABASE_URL: str | None = None
    # Por defecto, SQLite en /data (persistente en Railway si montas volume; y no falla por permisos)
    DB_PATH: str = "/data/brands.db"
    # Ajusta luego con el dominio de Vercel si quieres restringir
    CORS_ORIGINS: str = "*"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
