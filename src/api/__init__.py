from fastapi import APIRouter, Security

from src.api.controllers import reading
# from src.core.sso.cloud import azure_scheme

api_router = APIRouter()

api_router.include_router(reading.router, prefix='/reading', tags=["reading"])
# api_router.include_router(admin.router, prefix="/admin", tags=["admin"], dependencies=[Security(azure_scheme)])
