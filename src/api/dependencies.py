from src.api.app import db_session_maker


def get_db():
    db = db_session_maker
    try:
        yield db
    finally:
        db.close()
