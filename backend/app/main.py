from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.audit import router as audit_router
from app.api.audit_store import router as audit_store_router
from app.api.audit_history import router as audit_history_router

from app.database.database import engine
from app.database.audit_model import AuditRecord

AuditRecord.metadata.create_all(bind=engine)

app = FastAPI(
    title="AegisMesh",
    version="0.2.0"
)

app.include_router(health_router)
app.include_router(audit_router)
app.include_router(audit_store_router)
app.include_router(audit_history_router)
