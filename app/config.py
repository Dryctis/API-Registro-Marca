# app/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ENV: str = "production"

    # Si está definida (e.g. Postgres), se usa. Si no, caemos a SQLite en /data.
    DATABASE_URL: str | None = None
    DB_PATH: str = "/data/brands.db"

    # Orígenes exactos permitidos (SIN "/" al final). Separa con coma.
    # Producción en Vercel + local:
    CORS_ORIGINS: str = "https://registro-marca-tau.vercel.app,http://localhost:3000"

    # Opcional: habilita previews de Vercel (*.vercel.app). Deja "" si no lo quieres.
    CORS_ORIGIN_REGEX: str = "https://.*\\.vercel\\.app"

    # Pydantic v2 settings
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

settings = Settings()
