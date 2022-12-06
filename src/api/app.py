import logging

from fastapi import APIRouter, FastAPI, status

from src.api.dependencies import engine
from src.api.routers import user, redis
from src.utils.settings import get_settings

settings = get_settings()

# TODO: init logger
# log = logging.getLogger()


app = FastAPI(
    title="Gonoma's website API",
    version='0.1.0',
    openapi_tags=[
        {
            'name': 'user',
            "description": "Operations with users. The **login** logic is also here.",
        },
        {
            "name": "items",
            "description": "Manage items. So _fancy_ they have their own docs.",
            "externalDocs": {
                "description": "Items external docs",
                "url": "https://fastapi.tiangolo.com/",
            },
        },
    ]
)


@app.on_event('startup')
async def startup() -> None:

    # TODO: add middlewares here like Prometheus for monitoring, BrotliMiddleware, CORSMiddleware

    # Routers
    v1_router = APIRouter(prefix='/v1')
    v1_router.include_router(user.router, tags=['user'])
    v1_router.include_router(redis.router, tags=['redis'])

    app.include_router(v1_router)


@app.on_event('shutdown')
async def shutdown() -> None:
    await engine.dispose()
