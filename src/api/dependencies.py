from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from src.utils.settings import get_settings

settings = get_settings()


# Set up DB session
engine = create_async_engine(settings.DB_URL, echo=False, poolclass=NullPool)

# The sessionmaker factory generates new Session objects when called
db_session_maker = sessionmaker(bind=engine,
                                autocommit=False,
                                autoflush=False,
                                expire_on_commit=False,
                                class_=AsyncSession,
                                )


def get_db():
    db = db_session_maker
    try:
        yield db
    finally:
        db.close()
