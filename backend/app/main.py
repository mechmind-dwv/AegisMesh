from fastapi import FastAPI

app = FastAPI(title="AegisMesh")

@app.get("/health")
def health():
    return {"status": "ok"}
