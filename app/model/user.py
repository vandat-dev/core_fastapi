from cloudinary.provisioning import users
from sqlalchemy import (Column, String, Integer)
from sqlalchemy.orm import relationship

from app.model.base import Base


class User(Base):
    __tablename__ = "test_user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(42), nullable=False)
    email = Column(String(255), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
