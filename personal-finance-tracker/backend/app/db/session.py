from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from typing import AsyncGenerator

# Create an async engine
async_engine = create_async_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True, # Test connections prior to handing them out
    # echo=True, # Uncomment for debugging SQL queries
)

# Create a sessionmaker for async sessions
AsyncSessionFactory = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False, # Keep objects accessible after commit
    autoflush=False,
    autocommit=False,
)

async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency to get an async database session."""
    async with AsyncSessionFactory() as session:
        try:
            yield session
            await session.commit() # Commit changes if no exceptions
        except Exception:
            await session.rollback() # Rollback on error
            raise
        finally:
            await session.close() 