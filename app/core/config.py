from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "MindEase API"
    jwt_secret_key: str = "CHANGE_ME"  # Should be overridden in .env
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24 * 7  # 1 week
    sqlite_db_file: str = "sqlite:///./mindease.db"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()
