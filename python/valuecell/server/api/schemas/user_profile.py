from datetime import datetime
from typing import List

from pydantic import BaseModel, Field

class UserProfileData(BaseModel):
    """User profile data schema."""

    id: int = Field(..., description="Profile ID")
    user_id: str = Field(..., description="User ID")
    category: str = Field(..., description="Profile category")
    content: str = Field(..., description="Profile content")
    created_at: datetime = Field(..., description="Profile creation timestamp")
    updated_at: datetime = Field(..., description="Profile last update timestamp")