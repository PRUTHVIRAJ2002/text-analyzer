from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Cloud Text Analysis Service")

app.include_router(router)
