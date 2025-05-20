import logging
from typing import Optional, List

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user import UserCreate, UserUpdate
from .base import CRUDBase
from ..model import User

logger = logging.getLogger(__name__)


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    @staticmethod
    async def get_user_by_id(db: AsyncSession, user_id: int) -> Optional[User]:
        query = select(User).where(User.id == user_id)
        result = await db.execute(query)
        return result.scalars().first()

    @staticmethod
    async def get_list_user(db: AsyncSession) -> List[dict]:
        query = select(User)
        result = await db.execute(query)
        users = result.scalars().all()
        return users


crud_user = CRUDUser(User)
