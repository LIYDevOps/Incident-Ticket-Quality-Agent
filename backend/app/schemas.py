from pydantic import BaseModel
from typing import Optional


class IncidentPayload(BaseModel):
    incident_number: str

    short_description: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    priority: Optional[str] = None
    assignment_group: Optional[str] = None
    cmdb_ci: Optional[str] = None
