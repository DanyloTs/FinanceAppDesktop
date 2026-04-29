import os
import urllib.parse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

def _require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(
            f"Required environment variable '{name}' is not set. "
            "Set it before starting the application (e.g. via a .env file)."
        )
    return value

DB_USER = _require_env("DB_USER")
DB_PASSWORD = urllib.parse.quote_plus(_require_env("DB_PASSWORD"))
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "3306")
DB_NAME = os.environ.get("DB_NAME", "finance")

_echo_raw = os.environ.get("DB_ECHO", "false").strip().lower()
DB_ECHO = _echo_raw in ("1", "true", "yes")

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    echo=DB_ECHO,
)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
