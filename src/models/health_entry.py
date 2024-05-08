from enum import Enum
from typing import Any
from typing import Dict
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class HealthStatus(Enum):
    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"
    READY = "Ready"
    LOADING = "Loading"
    STOPPED = "Stopped"

    def __str__(self):
        return self.value


class HealthEntry(BaseModel):
    """
    Health entry
    """

    data: Dict[str, Any] = Field({}, alias="Data")
    description: Optional[str] = Field(None, alias="Description")
    ready_time: Optional[str] = Field(None, alias="ReadyTime")
    duration: Optional[str] = Field("0(days) 00:00:00.0000000", alias="Duration")
    status: HealthStatus = Field(alias="Status")

    def dict(self, by_alias=True, **kwargs):
        return super().dict(by_alias=by_alias, **kwargs)
