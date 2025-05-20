from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    # Postgres
    POSTGRES_USER: str='admin'
    POSTGRES_PASSWORD: str='123123'
    POSTGRES_DB: str='fast_api_demo'
    POSTGRES_PORT: str='5001'
    POSTGRES_HOST: str='172.17.0.1'
    DEBUG: Optional[bool] = False

    # Email
    COURSE_EMAIl: str = 'datbe26092001@gmail.com'
    COURSE_EMAIL_PASSWORD: str ='datttttt'

    # Jwt
    ACCESS_TOKEN_EXPIRES_IN_DAYS: int = 7
    REFRESH_TOKEN_EXPIRES_IN_DAYS: int = 10
    JWT_ALGORITHM: str = 'HS256'
    JWT_SECRET_KEY: str = 'eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY4MTY1NTk4OCwiaWF0IjoxNjgxNjU1OTg4fQ.ADE6-a6XcA3R5hVZiiY1mCUkj82HjADzCXBrUaRurFk'

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        # Regular URI format for use with asyncpg
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    @property
    def ASYNC_SQLALCHEMY_DATABASE_URI(self) -> str:
        # Async URI format uses the asyncpg driver
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
