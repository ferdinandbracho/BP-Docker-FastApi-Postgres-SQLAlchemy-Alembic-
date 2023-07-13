from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.config import config
from app.api.api_v1.api import api_router

app = FastAPI(
    title=config.PROJECT_NAME
)

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router)
