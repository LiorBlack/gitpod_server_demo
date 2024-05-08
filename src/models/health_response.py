from typing import Dict
from typing import Optional

from models.health_entry import HealthEntry
from models.health_entry import HealthStatus
from pydantic import BaseModel
from pydantic import Field


class HealthResponse(BaseModel):
    """
    Health response
    """

    entries: Dict[str, HealthEntry] = Field(alias="Entries")
    status: HealthStatus = Field(alias="Status")
    up_time: Optional[str] = Field(None, alias="UpTime")
    total_duration: Optional[str] = Field(
        "0(days) 00:00:00.0000000", alias="TotalDuration"
    )

    def json(self, by_alias=True, **kwargs):
        return super().json(by_alias=by_alias, **kwargs)
