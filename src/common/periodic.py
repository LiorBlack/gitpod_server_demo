from asyncio import Task, create_task, sleep
from typing import Callable, Coroutine
from loguru import logger


def periodic_async(interval: int) -> Callable[..., Callable[..., Task]]:
    def scheduler(func: Callable[..., Coroutine]) -> Callable[..., Task]:
        def wrapper(*args, **kwargs) -> Task:
            async def periodic() -> None:
                while True:
                    logger.trace(
                        f"Running {func.__name__} periodically, every {interval} seconds"
                    )
                    await func(*args, **kwargs)
                    await sleep(interval)

            return create_task(periodic())

        return wrapper

    return scheduler
