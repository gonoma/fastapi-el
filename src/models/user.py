from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(UserBase):
    hashed_password: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: str
