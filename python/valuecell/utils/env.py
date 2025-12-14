"""Utilites for resolving environment variables."""
import os
from pathlib import Path

def get_system_env_dir() -> Path:
    """
    Return the OS user configuration directory for ValueCell

    """
    home = Path.home()
    if os.name == "nt":
        appdata = os.getenv("APPDATA")
        base = Path(appdata) if appdata else home / "AppData" / "Roaming"
        return base / "ValueCell"
    if sys_platform_is_darwin():
        return home / "Library" / "Application Support" / "ValueCell"
    return home / ".config" / "valuecell"


def sys_platform_is_darwin() -> bool:
    """Detect if the system platform is Darwin (macOS)."""
    try:
        import sys
        return sys.platform == "darwin"
    except Exception:
        return False