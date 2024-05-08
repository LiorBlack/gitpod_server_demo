import re
from pathlib import Path
from typing import Any

import uvicorn
from common.environment import ALLOWED_ORIGINS
from common.environment import APP_TITLE
from common.environment import ENV
from common.environment import PORT
from common.environment import VERSION
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import UJSONResponse
from loguru import logger
from routers import health
from routers import swagger

logger.add("logs/app.log")


def _resolve_path(path: str) -> Path:
    dir_path = Path(__file__).resolve().parent
    return dir_path.joinpath(path)


def _resolve_port(port: str) -> int:
    try:
        return int(port if re.match(r"^{.*}$", port) is None else "8080")
    except Exception as err:
        logger.error(f"Could not parse PORT: {port}, using 8080 instead. Error {err}")
        return 8000


def _resolve_app(env: str) -> Any:
    return "main:app" if env == "local" else app


def _resolve_host(env: str) -> str:
    return "0.0.0.0"


def _load_description() -> str:
    with open(_resolve_path("../DESCRIPTION.md"), "r", encoding="utf-8") as readme:
        return readme.read()


app = FastAPI(
    title=APP_TITLE,
    description=_load_description(),
    version=f"{VERSION}-{ENV}",
    docs_url=None,
    default_response_class=UJSONResponse,
)

origins = ALLOWED_ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/health")
app.include_router(swagger.router)

if __name__ == "__main__":
    uvicorn.run(  # pragma: no cover
        _resolve_app(env=ENV),
        host=_resolve_host(env=ENV),
        headers=[("server", "template")],
        reload=ENV == "local",
        port=_resolve_port(port=PORT),
    )
