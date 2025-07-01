from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import POSTGRES_USER, POSTGRES_DATABASE, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT
from sqlalchemy import select, text, Row, insert, update, delete

DATABASE_URL = (f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:"
                f"{POSTGRES_PORT}/{POSTGRES_DATABASE}")

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()
