from fastapi import FastAPI

app = FastAPI(
    title="Personal Finance Tracker API",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy"} 