from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.audit import router as audit_router

app = FastAPI(
    title="AegisMesh",
    version="0.1.0"
)

app.include_router(health_router)
app.include_router(audit_router)
