from pydantic import BaseModel

class AuditReport(BaseModel):
    risk_score: int
    tracked_services: list[str]
    recommendations: list[str]
