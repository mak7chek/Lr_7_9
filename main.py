from fastapi import FastAPI
from external_api.router import router as external_router

app = FastAPI(title="Humor API Lab")

app.include_router(external_router)

@app.get("/")
def read_root():
    return {"message": "Server is running! Go to /docs to see the API."}