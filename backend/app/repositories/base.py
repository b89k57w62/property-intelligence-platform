"""Base Repository - Generic Data Access Layer Base Class"""

from typing import Generic, TypeVar, Type, Optional
from sqlalchemy.orm import Session
from app.core.database import Base


# Define generic constraint: only accept ORM Models that inherit from Base
ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    """
    Generic Repository Base Class

    Provides basic CRUD operations that all repositories can inherit from.

    Example:
        class PropertyRepository(BaseRepository[Property]):
            def __init__(self, db: Session):
                super().__init__(Property, db)
    """

    def __init__(self, model: Type[ModelType], db: Session):
        """
        Initialize Repository

        Args:
            model: ORM Model class (must inherit from Base)
            db: SQLAlchemy Session instance
        """
        self.model = model
        self.db = db

    def get(self, id: int) -> Optional[ModelType]:
        """
        Query single record by ID

        Args:
            id: Primary key ID of the record

        Returns:
            Model instance if found, None otherwise

        Example:
            repo = PropertyRepository(db)
            property = repo.get(1)
            if property:
                print(property.city)
        """
        return self.db.query(self.model).filter(self.model.id == id).first()
