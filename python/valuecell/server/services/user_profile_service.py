"""user profile service."""

import logging
from typing import Dict, List, Optional

from ..db.models.user_profile import ProfileCategory 
from ..db.repositories.user_profile_repository  import UserProfileRepository

logger =logging.getLogger(__name__)

class UserProfileService:
    """Service class for user profile management."""
    #TODO: implement methods

    def get_user_profiles(
            self,
            user_id: str,
            category: Optional[str] = None
            ) -> List[Dict]:
        """
        Docstring for get_user_profiles
        
        :param self: Description
        :param user_id: Description
        :type user_id: str
        :param category: Description
        :type category: Optional[str]
        :return: Description
        :rtype: List[Dict]
        """
        try:
            profile_category = None
            if category:
                profile_category = self._validate_category(category)
                if not profile_category:
                    logger.error(f"Invalid profile category: {category}")
                    return []
            profiles = self.repository.get_profiles_by_user(user_id, profile_category)
            return [profile.to_dict() for profile in profiles]
        except Exception as e:
            logger.error(f"Error retrieving user profiles: {e}")
            return []
        
    

_user_profile_service: Optional["UserProfileService"] = None

def get_user_profile_service() -> "UserProfileService":
    """Get global user profile service instance."""
    global _user_profile_service
    if _user_profile_service is None:
        _user_profile_service = UserProfileService()
    return _user_profile_service