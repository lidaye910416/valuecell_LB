from typing import List, Optional

from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..connection import get_database_manager
from ..models.user_profile import UserProfile, ProfileCategory

class UserProfileRepository:
    """Repository for user profile data."""

    def __init__(self, db_session: Optional[Session] = None):
        """Initialize repository with database session."""
        self.db_session = db_session

    def _get_session(self) -> Session:
        """Get database session."""
        pass

    def create_profile() -> Optional[UserProfile]:
        """Create a new user profile."""
        pass

    def get_profile(self, profile_id: int, uesr_id: str) -> Optional[UserProfile]:
        """Get a specific user profile by ID and user ID."""
        pass

    def get_profiles_by_user(
            self, 
            user_id: str,
            catagory: Optional[ProfileCategory] = None,
    ) -> List[UserProfile]:
        """Get all profiles for a specific user, optionally filtered by category."""
        pass

    def update_profile(
            self,
            profile_id: int,
            user_id: str,
            content: str,
    ) -> Optional[UserProfile]:
        """Update an existing user profile's content."""
        pass