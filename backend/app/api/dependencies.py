"""FastAPI dependency injection utilities."""

from typing import Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db


def get_current_user():
    """
    Dependency for getting current authenticated user.
    Placeholder for future authentication implementation.
    """
    # TODO: Implement JWT token validation
    pass


def get_pagination_params(
    skip: int = 0,
    limit: int = 20,
) -> dict:
    """
    Dependency for pagination parameters.

    Args:
        skip: Number of records to skip
        limit: Maximum number of records to return

    Returns:
        Dictionary with pagination parameters
    """
    if skip < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Skip parameter must be non-negative"
        )
    if limit <= 0 or limit > 100:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Limit must be between 1 and 100"
        )
    return {"skip": skip, "limit": limit}
