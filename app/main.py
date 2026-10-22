from fastapi import FastAPI

app = FastAPI(
    title="fastAPI components",
    description="Adding fastAPI components to make meaningful app",
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health():
    return {"status": "ok"}

#uv run fastapi dev