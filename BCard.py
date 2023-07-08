from fastapi import FastAPI
from routes.bcardroute import BCardrouter
from fastapi import FastAPI

description=""

app = FastAPI(
    title="BCard",
    version="v1.0",
    description=description,
    redoc_url=None
)

app.include_router(BCardrouter)