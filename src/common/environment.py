import json
import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from loguru import logger

load_dotenv(dotenv_path="config/.env-local")


def _str_to_bool(value: str) -> bool:
    return value.lower() in ("yes", "true", "1")


def _safe_print(value: Optional[str], key: str) -> Optional[str]:
    if value is None:
        return None
    if any(check in key for check in ["KEY", "TOKEN", "SECRET", "PASS"]):
        return "".join("*" for _ in value)
    return value


def _get_all_variables():
    module = globals()
    return {
        key: _safe_print(value, key)
        for key, value in module.items()
        if not key.startswith("__") and not key.startswith("_") and key.isupper()
    }


# General
ENV = os.environ.get("ENV", "local")
PORT = os.environ.get("PORT", "8080")
VERSION = os.environ.get("VERSION")
APP_TITLE = os.environ.get("APP_TITLE", "FastAPI Example")
HTML_TEMPLATE_DIR: Path = Path(__file__).parent.parent.parent.joinpath(
    os.environ.get("HTML_TEMPLATE_DIR", "html_templates")
)

# Security
ALLOWED_ORIGINS: list = (
    []
    if not os.environ.get("ALLOWED_ORIGINS")
    else os.environ.get("ALLOWED_ORIGINS", "").split(",")
)
OAUTH_REQUIRED_SCOPES = os.environ.get("OAUTH_REQUIRED_SCOPES", "scopes").split(",")
OAUTH_IDENTITY_SERVER_URL = os.environ.get("OAUTH_IDENTITY_SERVER_URL", "")
OAUTH_CLIENT_ID = os.environ.get("OAUTH_CLIENT_ID", "client_id")
OAUTH_CLIENT_SECRET = os.environ.get("OAUTH_CLIENT_SECRET", "secret")
AUTHENTICATION_DISABLED = _str_to_bool(
    os.environ.get("AUTHENTICATION_DISABLED", "False")
)
REQUESTS_CA_BUNDLE = os.environ.get("REQUESTS_CA_BUNDLE", "")

# Log environment
ENVIRONMENT = _get_all_variables()

logger.info(json.dumps(ENVIRONMENT, indent=2, sort_keys=True, default=str))
