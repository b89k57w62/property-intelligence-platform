"""Data access repositories."""

from app.repositories.base import BaseRepository
from app.repositories.property_repository import PropertyRepository

__all__ = ["BaseRepository", "PropertyRepository"]
