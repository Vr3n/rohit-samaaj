from functools import lru_cache
from os import getenv
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    if (db := getenv("POSTGRES_DB")) is not None:
        settings.database_url = PostgresDsn.build(
            schema="postgresql",
            user=settings.database_url.user,
            password=settings.database_url.password,
            host=settings.database_url.host,
            port=settings.database_url.port,
            path=f"/{db}"
        )
    return settings
