from datetime import timedelta
import json
import sys

from fastapi import APIRouter
import httpx
import redis


router = APIRouter(prefix='/redis')

# URL tutorial -> https://rednafi.github.io/digressions/python/database/2020/05/25/python-redis-cache.html

def redis_connect() -> redis.client.Redis:
    try:
        client = redis.Redis(
            host="localhost",
            port=6379,
            # password="ubuntu",
            db=0,
            socket_timeout=5,
        )
        ping = client.ping()
        if ping is True:
            return client
    except redis.AuthenticationError:
        print("AuthenticationError")
        sys.exit(1)


client = redis_connect()


def get_routes_from_api(parameters: str) -> dict:
    """Data from mapbox api."""

    with httpx.Client() as client:
        # base_url = "https://api.mapbox.com/optimized-trips/v1/mapbox/driving"
        # geometries = "geojson"
        # access_token = "Your-MapBox-API-token"
        # url = f"{base_url}/{coordinates}?geometries={geometries}&access_token={access_token}"

        'https://ipinfo.io/161.185.160.93/geo'

        # Name
        url = f'https://api.nationalize.io/?name={parameters}'

        # Yoda; max 5 requests per hour
        # url = f'https://api.funtranslations.com/translate/yoda.json?text={parameters}'

        response = client.get(url)

        return response


def get_routes_from_cache(key: str) -> str:
    """Data from redis."""

    val = client.get(key)
    return val


def set_routes_to_cache(key: str, value: str) -> bool:
    """Data to redis."""

    state = client.setex(key, timedelta(seconds=3600), value=value,)
    return state


def route_optima(parameters: str) -> dict:

    # First it looks for the data in redis cache
    data = get_routes_from_cache(key=parameters)

    # If cache is found then serves the data from cache
    if data is not None:
        data = json.loads(data)
        data["cache"] = True
        return data

    else:
        # If cache is not found then sends request to the MapBox API
        response = get_routes_from_api(parameters)

        # This block sets saves the respose to redis and serves it directly
        if response.status_code == 200:
            data = response.json()
            data["cache"] = False
            data = json.dumps(data)
            state = set_routes_to_cache(key=parameters, value=data)

            if state is True:
                return json.loads(data)
        return data


@router.get("/route-optima/{parameters}")
def view(parameters: str) -> dict:
    """This will wrap our original route optimization API and
    incorporate Redis Caching. You'll only expose this API to
    the end user. """

    # For Yoda
    # parameters = parameters.replace(" ", "%20")

    return route_optima(parameters)
