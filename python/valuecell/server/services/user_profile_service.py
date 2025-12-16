"""user profile service."""

import logging
from typing import Dict, List, Optional

from ..db.models.user_profile import ProfileCategory 
from ..db.repositories.user_profile_repository  import UserProfileRepository


class UserProfileService:
    """Service class for user profile management."""
    #TODO: implement methods
    pass

_user_profile_service: Optional["UserProfileService"] = None

def get_user_profile_service() -> "UserProfileService":
    """Get global user profile service instance."""
    global _user_profile_service
    if _user_profile_service is None:
        _user_profile_service = UserProfileService()
    return _user_profile_service