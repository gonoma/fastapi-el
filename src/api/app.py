import logging

from fastapi import APIRouter, FastAPI, status

from src.api.dependencies import engine
from src.api.routers import user
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

    app.include_router(v1_router)


@app.on_event('shutdown')
async def shutdown() -> None:
    await engine.dispose()




# app.py

# import json
# import sys
# from datetime import timedelta
#
# import httpx
# import redis
# from fastapi import FastAPI
#
#
#
# def redis_connect() -> redis.client.Redis:
#     try:
#         client = redis.Redis(
#             host="localhost",
#             port=6379,
#             password="ubuntu",
#             db=0,
#             socket_timeout=5,
#         )
#         ping = client.ping()
#         if ping is True:
#             return client
#     except redis.AuthenticationError:
#         print("AuthenticationError")
#         sys.exit(1)
#
#
# client = redis_connect()
#
#
# def get_routes_from_api(coordinates: str) -> dict:
#     """Data from mapbox api."""
#
#     with httpx.Client() as client:
#         base_url = "https://api.mapbox.com/optimized-trips/v1/mapbox/driving"
#
#         geometries = "geojson"
#         access_token = "Your-MapBox-API-token"
#
#         url = f"{base_url}/{coordinates}?geometries={geometries}&access_token={access_token}"
#
#         response = client.get(url)
#         return response.json()
#
#
# def get_routes_from_cache(key: str) -> str:
#     """Data from redis."""
#
#     val = client.get(key)
#     return val
#
#
# def set_routes_to_cache(key: str, value: str) -> bool:
#     """Data to redis."""
#
#     state = client.setex(key, timedelta(seconds=3600), value=value,)
#     return state
#
#
# def route_optima(coordinates: str) -> dict:
#
#     # First it looks for the data in redis cache
#     data = get_routes_from_cache(key=coordinates)
#
#     # If cache is found then serves the data from cache
#     if data is not None:
#         data = json.loads(data)
#         data["cache"] = True
#         return data
#
#     else:
#         # If cache is not found then sends request to the MapBox API
#         data = get_routes_from_api(coordinates)
#
#         # This block sets saves the respose to redis and serves it directly
#         if data.get("code") == "Ok":
#             data["cache"] = False
#             data = json.dumps(data)
#             state = set_routes_to_cache(key=coordinates, value=data)
#
#             if state is True:
#                 return json.loads(data)
#         return data
#
#
# app = FastAPI()
#
#
# @app.get("/route-optima/{coordinates}")
# def view(coordinates: str) -> dict:
#     """This will wrap our original route optimization API and
#     incorporate Redis Caching. You'll only expose this API to
#     the end user. """
#
#     # coordinates = "90.3866,23.7182;90.3742,23.7461"
#
#     return route_optima(coordinates)