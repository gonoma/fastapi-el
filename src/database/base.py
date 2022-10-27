import sqlalchemy.schema
from sqlalchemy import inspect
from sqlalchemy.orm import as_declarative


@as_declarative(metadata=sqlalchemy.schema.MetaData(naming_convention={
    "ix": "%(column_0_label)s_idx",
    "uq": "%(table_name)s_%(column_0_name)s_key",
    "ck": "%(table_name)s_%(constraint_name)s_check",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey"
}))
class BaseModel:
    __mapper_args__ = {'eager_defaults': True}

    def __init__(self, *args: ..., **kwargs: ...) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        data = ', '.join([f'{key}={repr(getattr(self, key))}' for key in inspect(self.__class__).columns.keys()])
        return f'<{self.__class__.__name__} {data}>'
