from enum import Enum

from datetime import date
from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel


class UserBase(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None

    class Config:
        orm_mode = True


class UserCreateParams(BaseModel):
    email: str
    username: str


class UserUpdateParams(BaseModel):
    username: Optional[str] = None


class UserCreate(BaseModel):
    id: int
    email: str
    username: str


class UserUpdate(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    full_name: Optional[str] = None


class LoginUser(BaseModel):
    email: str
    password: str


class UserInfo(BaseModel):
    id: int
    username: Optional[str] = None
    email: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        orm_mode = True


class UserResponse(UserBase):
    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: str(v.timestamp())
        }
