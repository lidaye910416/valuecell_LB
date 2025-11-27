from pydantic_settings import BaseSettings
from typing import List

class Setttings(BaseSettings):
    """Server configuration settings."""

    # Application Configuration
    APP_NAME: str = "ValueCell Server"  #应用名称
    API_HOST: str = "0.0.0.0"           # API主机地址
    APP_VERSION: str = "0.1.0"          # 应用版本
    APP_ENVIRONMENT: str = "development"# 应用环境
    API_PORT: int = 8000                # API端口
    API_DEBUG: bool = True              # API调试模式
    CORS_ORIGINS: List[str] = ["http://localhost", "http://localhost:3000"] # 允许的前端跨域地址


def get_settings() -> Setttings:
    """Get cached settings instance."""
    return Setttings()