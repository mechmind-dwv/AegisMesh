from fastapi import APIRouter

from app.services.audit_repository import AuditRepository

router = APIRouter(
    prefix="/audit-store",
    tags=["audit-store"]
)

@router.get("/history")
def audit_history():

    return AuditRepository().all()
