"""Data access repositories."""

from app.repositories.base import BaseRepository
from app.repositories.property_transaction_repository import (
    PropertyTransactionRepository,
)
from app.repositories.property_presale_repository import PropertyPresaleRepository
from app.repositories.property_rental_repository import PropertyRentalRepository

__all__ = [
    "BaseRepository",
    "PropertyTransactionRepository",
    "PropertyPresaleRepository",
    "PropertyRentalRepository",
]
