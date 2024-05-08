from typing import Any
from typing import Dict
from typing import Union

from models.health_entry import HealthStatus

HEALTH_RESPONSES: Dict[Union[int, str], Dict[str, Any]] = {
    200: {
        "description": "Service is alive",
        "content": {
            "application/json": {
                "example": {
                    "Entries": {
                        "Liveness": {
                            "Data": {"Version": "1.1.0.43"},
                            "Duration": "12(days) 00:00:00.0000028",
                            "Status": HealthStatus.HEALTHY,
                        }
                    },
                    "Status": HealthStatus.HEALTHY,
                    "TotalDuration": "12(days) 00:00:00.0000139",
                }
            }
        },
    }
}


READINESS_RESPONSES: Union[Dict[Union[int, str], Dict[str, Any]], None] = {
    200: {
        "description": "Service is ready",
        "content": {
            "application/json": {
                "example": {
                    "Entries": {
                        "IdentityServer": {
                            "Data": {},
                            "Duration": "12(days) 00:00:00.1089549",
                            "Status": HealthStatus.READY,
                        },
                        "DataSourceHealthCheck": {
                            "Data": {},
                            "Description": "Data source is healthy and ready.",
                            "Duration": "12(days) 00:00:00.0841640",
                            "Status": HealthStatus.READY,
                        },
                    },
                    "Status": HealthStatus.HEALTHY,
                    "TotalDuration": "12(days) 00:00:00.1932015",
                }
            }
        },
    },
    503: {
        "description": "Service is not ready",
        "content": {
            "application/json": {
                "example": {
                    "Entries": {
                        "IdentityServer": {
                            "Data": {},
                            "Duration": "12(days) 00:00:00.1089549",
                            "Status": HealthStatus.LOADING,
                        }
                    },
                    "Status": HealthStatus.UNHEALTHY,
                    "TotalDuration": "12(days) 00:00:00.1932015",
                }
            }
        },
    },
}
