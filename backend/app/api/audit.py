from fastapi import APIRouter
from app.services.audit_engine import AuditEngine

router = APIRouter(prefix="/audit", tags=["audit"])

@router.get("/")
def audit():

    engine = AuditEngine()

    return engine.run()
