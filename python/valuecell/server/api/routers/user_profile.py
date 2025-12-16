from typing import Optional
from fastapi import APIRouter, HTTPException, Path, Query

from ..schemas import SuccessResponse
from ...db.models.user_profile import ProfileCategory

from ...services.user_profile_service import get_user_profile_service

from ..schemas import (
    UserProfileData,
    CreateUserProfileRequest,
)

DEFAULT_USER_ID = "default_user"

def create_user_profile_router() -> APIRouter:
    """Create user profile related routes."""

    router = APIRouter(prefix="/user/profile", tags=["User Profile"])

    # Get service dependency
    #profile_service = get_user_profile_service() #解耦

    @router.post(
        "",
        response_model=SuccessResponse[UserProfileData],
        summary="Create user profile",
        description="Create a new user profile with specified category and content",)

    async def create_user_profile(request: CreateUserProfileRequest):
        """Create a new user profile."""
        try:
            # Use default user ID for now
            user_id = DEFAULT_USER_ID

            #Validate category
            valid_categories = [e.value for e in ProfileCategory]
            if request.category not in valid_categories:
                raise HTTPException(status_code=400, detail=f"Invalid category. Valid categories are: {valid_categories}")

            # Create profile logic here
            profile = profile_service.create_profile()
            