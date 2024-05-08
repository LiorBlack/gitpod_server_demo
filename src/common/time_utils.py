import time
from datetime import datetime
from functools import wraps

from loguru import logger


def get_today_formatted() -> str:
    return datetime.today().strftime("%Y-%m-%d")


def pretty_time_delta(tim: float) -> str:
    seconds = int(tim)
    rest = int((tim - seconds) * 1e7)
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return f"{days}(days) {hours:0>2}:{minutes:0>2}:{seconds:0>2}.{rest:0>7}"


def timeit_async(func):
    @wraps(func)
    async def wrapped(*args, **kwargs):
        start = time.perf_counter()
        result = await func(*args, **kwargs)
        end = time.perf_counter()
        logger.debug(
            f"Function {func.__name__} executed in {pretty_time_delta(end - start)}"
        )
        return result

    return wrapped


def timeit(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        logger.debug(
            f"Function {func.__name__} executed in {pretty_time_delta(end - start)}"
        )
        return result

    return wrapped
