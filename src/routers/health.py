from typing import Dict

from common.environment import ENVIRONMENT
from common.environment import VERSION
from common.health_response_wrapper import get_live_time
from common.health_response_wrapper import wrap_health_response
from common.time_utils import timeit
from fastapi import APIRouter
from fastapi import Request
from models.health_doc import HEALTH_RESPONSES
from models.health_doc import READINESS_RESPONSES
from models.health_entry import HealthEntry
from models.health_entry import HealthStatus
from models.health_response import HealthResponse

router = APIRouter()


@timeit
def _get_liveness_object() -> Dict[str, HealthEntry]:
    liveness = HealthEntry(
        Data={"Version": VERSION, "Environment": ENVIRONMENT},
        Status=HealthStatus.HEALTHY,
        ReadyTime=get_live_time(),
        Description="Returns version and liveness of service",
        Duration=None,
    )
    return {"Liveness": liveness}


@router.get(
    "/liveness",
    response_model=HealthResponse,
    tags=["Health Checks"],
    responses=HEALTH_RESPONSES,
    summary="Checks if service is alive",
)
@wrap_health_response
async def get_liveness() -> Dict[str, HealthEntry]:
    return _get_liveness_object()


@router.get(
    "/readiness",
    response_model=HealthResponse,
    tags=["Health Checks"],
    responses=READINESS_RESPONSES,
    summary="Checks if service is ready",
)
@wrap_health_response
async def get_readiness(request: Request) -> Dict[str, HealthEntry]:
    readiness = HealthEntry(
        Data={"Exposed URL's": [route.path for route in request.app.routes]},
        Status=HealthStatus.READY,
        Description="Template Readiness entry",
        Duration=None,
        ReadyTime=None,
    )
    return {"Readiness": readiness}
