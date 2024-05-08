import json
import time
from functools import wraps

from common.time_utils import pretty_time_delta
from fastapi.responses import JSONResponse
from models.health_entry import HealthStatus
from models.health_response import HealthResponse

LIVE_START_TIME = time.time()


def get_live_time():
    return pretty_time_delta(time.time() - LIVE_START_TIME)


def _set_overall_health(base_response: HealthResponse):
    for entry in base_response.entries.values():
        if hasattr(entry, "status") and entry.status == HealthStatus.UNHEALTHY:
            base_response.status = HealthStatus.UNHEALTHY
            break


def wrap_health_response(func):
    @wraps(func)
    async def inject_health_response(*args, **kwargs):
        start = time.time()
        base_response = HealthResponse(
            Entries={}, Status=HealthStatus.HEALTHY, UpTime=None, TotalDuration=None
        )
        base_response.entries = await func(*args, **kwargs)
        _set_overall_health(base_response)
        base_response.up_time = get_live_time()
        base_response.total_duration = pretty_time_delta(time.time() - start)
        return JSONResponse(content=json.loads(base_response.json()))

    return inject_health_response
