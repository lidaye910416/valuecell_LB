from pydantic import BaseModel, Field
from enum import IntEnum
from typing import Generic, TypeVar, Optional

T = TypeVar("T")

class StatusCode(IntEnum):
    """Unified API status code enumeration."""

    # Success status codes
    SUCCESS = 0

    # Client error status codes
    BAD_REQUEST = 400  # Bad request parameters
    UNAUTHORIZED = 401  # Unauthorized access
    FORBIDDEN = 403  # Forbidden access
    NOT_FOUND = 404  # Resource not found

    # Server error status codes
    INTERNAL_ERROR = 500  # Internal server error

class AppInfoData(BaseModel):
    """Application information model."""

    name: str = Field(..., description="Application name")
    version: str = Field(..., description="Application version")
    environment: str = Field(..., description="Application environment")


class BaseResponse(BaseModel, Generic[T]):
    """Unified API response base model"""

    code: int = Field(..., description="Status code")
    msg: str = Field(..., description="Response message")
    data: Optional[T] = Field(None, description="Response data")

class SuccessResponse(BaseResponse[T]):
    """Sucecess response model"""

    code: int = Field(default=StatusCode.SUCCESS, description="Success status code")
    msg: str = Field(default="success", description="Success message")
    data: Optional[T] = Field(None, description="Response data")

    @classmethod
    def create(cls, data: T = None, msg: str = "success") -> "SuccessResponse[T]":
        """Create success response."""
        return cls(code=StatusCode.SUCCESS, msg=msg, data=data)