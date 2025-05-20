import logging
from datetime import datetime

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.api.depend import oauth2
from app.db.database import get_db
from app.model import User
from app.schemas import UserCreateParams
from app.services.user import UserService
from app.utils.response import make_response_object

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/user/list_user")
async def get_list_users_async(db: Session = Depends(get_db)):
    user_service = UserService(db=db)
    print(f"Start")
    user_response = await user_service.get_list_users_async()
    print(f"End")
    return user_response


@router.get("/user/{user_id}/get_user")
async def get_user_by_id(user_id: int,
                         db: Session = Depends(get_db)):
    user_service = UserService(db=db)
    user_response = await user_service.get_user_by_id(user_id=user_id)
    return user_response


@router.get("/user/me")
async def read_me(user: User = Depends(oauth2.get_current_user),
                  db: Session = Depends(get_db)):
    user_service = UserService(db=db)
    user_response = await user_service.get_user_by_id(user_id=user.id)
    return user_response


@router.post("/user/create_user")
async def create_user(user_create: UserCreateParams,
                      db: Session = Depends(get_db)):
    user_service = UserService(db=db)
    user_response = await user_service.create_user(user_create=user_create)
    return make_response_object(user_response)
