from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # General
    ENV: Literal["development", "production"] = "development"
    DEBUG: bool = True

    # Secrets
    SECRET_KEY: str
    SESSION_SECRET_KEY: str

    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day

    # OAuth
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    GOOGLE_REDIRECT_URI: str

    # CORS
    ALLOWED_ORIGINS: list[str] = ["http://localhost:3000"]
    FRONTEND_URL: str

    # Database
    DATABASE_URL: str = "sqlite:///./dev.db"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
