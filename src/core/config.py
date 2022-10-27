from pydantic import BaseSettings, Field
from pydantic.tools import lru_cache


class Settings(BaseSettings):
    Env: str = Field('Dev', env='Env')
    DbHost: str = Field(env='DbHost')
    DbPort: str = Field(env='DbPort')
    DbName: str = Field(env='DbName')
    DbUser: str = Field(env='DbUser')
    DbPass: str = Field(env='DbPass')


@lru_cache()
def get_settings():
    """
    FastAPI dependency to get the settings instance.


    """
    return Settings()
