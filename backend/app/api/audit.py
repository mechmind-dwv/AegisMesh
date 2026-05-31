from fastapi import APIRouter

from app.models.audit import AuditReport
from app.services.audit_engine import AuditEngine

router = APIRouter(
    prefix="/audit",
    tags=["audit"]
)

@router.get("/", response_model=AuditReport)
def audit():

    engine = AuditEngine()

    return engine.run()
