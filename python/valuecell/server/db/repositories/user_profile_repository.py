from typing import List, Optional

from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..connection import get_database_manager
from ..models.user_profile import UserProfile, ProfileCategory

class UserProfileRepository:
    """Repository for user profile data."""


    def __init__(self, db_session: )
