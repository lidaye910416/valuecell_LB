"""Database connection and session mmaneger for ValueCell server."""

from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from ..config.settings import get_settings
from .models.base import Base

class DatabaseManager:
    """Database connection and session manager."""

    def __init__(self):
        """Database manager initialization."""
        self.settings = get_settings()
        self.engine = Engine = None
        self.SessionLocal = None
        self._initialize_database()

    def _initialize_database(self):
        """Initialize database manager"""
        database_config = self.settings.ge