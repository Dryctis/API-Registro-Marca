from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENV: str = "local"
    DATABASE_URL: str = "sqlite:///./brands.db"
    CORS_ORIGINS: str = "http://localhost:3000"

    class Config:
        env_file = ".env"

settings = Settings()
