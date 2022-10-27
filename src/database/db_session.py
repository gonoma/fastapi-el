# coding: utf-8
import logging
from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core.config import Settings

@lru_cache
def get_local_db_session(settings: Settings):
    logging.info("Creating session maker")
    sqlalchemy_database_url = f"postgresql://{settings.DbUser}:{settings.DbPass}@{settings.DbHost}:{settings.DbPort}/{settings.DbName}"
    engine = create_engine(sqlalchemy_database_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal
