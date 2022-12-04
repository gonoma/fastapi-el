from functools import lru_cache

from pydantic import BaseSettings, Field, PostgresDsn


class Settings(BaseSettings):
    ENV: str = Field(env='ENV', default='DEV')
    DB_URL: PostgresDsn = Field(env='DB_URL', default='postgres+asyncpg://user:password@postgresserver/db')
    CELERY_DB_URL: PostgresDsn = Field(env='CELERY_DB_URL', default='postgresql://user:password@postgresserver/db')
    BASE_URL: str = Field(env='BASE_URL', default='localhost:8000')
    SECRET_KEY: str = Field(env='SECRET_KEY')
    ALGORITHM: str = Field(env='ALGORITHM')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(env='ACCESS_TOKEN_EXPIRE_MINUTES')


@lru_cache
def get_settings() -> Settings:
    return Settings()
