"""Settings for the server application."""

import os
from functools import lru_cache # 缓存装饰器, 用于缓存函数的返回值, 提高性能

from pydantic_settings import BaseSettings
from typing import List
from pathlib import Path

from ...utils.env import get_system_env_dir

def _get_project_root() -> str:
    """Get the root directory of the project.
    
    Layout assumption: this file is at `project_root/python/valuecell/server/config/settings.py`
    we walk up 4 levels to reach the project root.
    """
    here = os.path.dirname(__file__)
    repository_root = os.path.abspath(
        os.path.join(here, "..", "..", "..", "..")
    )
    return repository_root

def _default_db_path() -> str:
    """Get default database DSN undeer the system application directory."""
    sys_dir = get_system_env_dir()

    db_path = Path(sys_dir) / "valuecell.db"
    return f"sqlite:///{db_path}"



class Setttings(BaseSettings):
    """Server configuration settings."""

    def __init__(self):
        
        #Application  Configurations
        self.APP_NAME: str = os.getenv("APP_NAME", "ValueCell Server")
        self.APP_VERSION: str = os.getenv("APP_VERSION", "0.1.0")

        #API configurations

        #CORS configurations

        #Database configurations

        # File Paths

        #I18N configurations




def get_settings() -> Setttings:
    """Get cached settings instance."""
    return Setttings()