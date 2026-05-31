from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {
        "project": "AegisMesh",
        "version": "0.1.0",
        "status": "running"
    }

@router.get("/health")
def health():
    return {"status": "ok"}
