from functools import lru_cache
from typing import AsyncIterator

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.core.settings import settings


@lru_cache()
def get_async_session_maker():
    # Use create_async_engine with the async URI
    engine = create_async_engine(
        settings.ASYNC_SQLALCHEMY_DATABASE_URI,
        echo=False
    )
    session_local = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
        class_=AsyncSession
    )
    return session_local


async def get_db() -> AsyncIterator[AsyncSession]:
    """Dependency for getting async database session"""
    session_local = get_async_session_maker()
    session = session_local()

    try:
        yield session
    except Exception as exc:
        await session.rollback()
        raise exc
    finally:
        await session.close()
