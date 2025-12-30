"""user profile service."""

import logging
from typing import Dict, List, Optional

from ..db.models.user_profile import ProfileCategory 
from ..db.repositories.user_profile_repository  import UserProfileRepository

logger = logging.getLogger(__name__) # configure logger

class UserProfileService:
    """Service class for user profile management."""
    def __init__(self, repository: Optional[UserProfileRepository] = None):
        """Initialize service with user profile repository."""
        self.repository = repository or UserProfileRepository()

    def create_profile(
            self, 
            user_id: str, 
            category: ProfileCategory, 
            content: str) -> Optional[Dict]:
        """Create a new user profile."""

        try:
            # Validate and conert category
            profile_category = self._validate_category(category)
            if not profile_category:
                logger.error(f"Invalid profile category: {category}")
                return None
            
            profile = self.repository.create_profile(
                user_id=user_id,
                category=profile_category,
                content=content,
            )

            if profile:
                logger.info(f"Created user profile with ID: {profile.id} for user: {user_id} with category: {category}")
                return profile.to_dict()

            return None
        
        except Exception as e:
            logger.error(f"Error creating user profile for user: {user_id} - {e}")
            return None


    def _validate_category(self, category: str) -> Optional[ProfileCategory]:
        """Validate and convert category string to ProfileCategory enum."""    

        try:
            return ProfileCategory(category)
        except ValueError:
            logger.error(f"Invalid profile category: {category}")
            return None 
        

    #TODO: implement methods
    pass

_user_profile_service: Optional["UserProfileService"] = None

def get_user_profile_service() -> "UserProfileService":
    """Get global user profile service instance."""
    global _user_profile_service
    if _user_profile_service is None:
        _user_profile_service = UserProfileService()
    return _user_profile_service