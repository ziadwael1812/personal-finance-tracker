from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column, Integer

@as_declarative()
class Base:
    """
    Base class for SQLAlchemy models.
    It includes an auto-generating ID primary key and a __tablename__ convention.
    """
    id = Column(Integer, primary_key=True, index=True)
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() 