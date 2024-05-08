import os
from functools import lru_cache
from pathlib import Path

import jinja2
from loguru import logger

MAX_CACHE_SIZE = 10


@lru_cache(maxsize=MAX_CACHE_SIZE)
def get_root_template_dir(temp_dir: str) -> Path:
    return Path(os.environ["PYTHONPATH"]).resolve().joinpath(temp_dir)


@lru_cache(maxsize=MAX_CACHE_SIZE)
def get_jinja_env(parent: Path) -> jinja2.Environment:
    logger.trace(parent)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(parent), autoescape=jinja2.select_autoescape()
    )
