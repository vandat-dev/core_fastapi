import logging

import redis
from sqlalchemy.ext.asyncio import AsyncSession

from ..crud.user import crud_user
from ..schemas import UserResponse, UserCreateParams

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self, db: AsyncSession):
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0)
        self.db = db

    async def get_user_by_id(self, user_id: int):
        current_user = await crud_user.get_user_by_id(db=self.db, user_id=user_id)
        if not current_user:
            return "not found"
        return UserResponse.from_orm(current_user)

    async def get_list_users_async(self):
        list_users = await crud_user.get_list_user(db=self.db)
        return list_users

    async def create_user(self, user_create: UserCreateParams):
        obj_in = UserCreateParams(**user_create.dict())
        current_user = await crud_user.create(db=self.db, obj_in=obj_in)
        return current_user
