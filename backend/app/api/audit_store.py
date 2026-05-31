from fastapi import APIRouter

from app.services.audit_engine import AuditEngine
from app.services.audit_repository import AuditRepository

router = APIRouter(
    prefix="/audit-store",
    tags=["audit-store"]
)

@router.post("/")
def store_audit():

    report = AuditEngine().run()

    record_id = AuditRepository().save(report)

    return {
        "stored": True,
        "id": record_id
    }
