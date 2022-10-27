# coding: utf-8

from fastapi import Depends

from src.core.config import Settings, get_settings
from src.database.db_session import get_local_db_session


def get_db(settings: Settings = Depends(get_settings)):

    SessionLocal = get_local_db_session(settings)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
