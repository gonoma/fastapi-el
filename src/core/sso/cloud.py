# # coding: utf-8
# from cachetools.func import lru_cache
# from fastapi_azure_auth import SingleTenantAzureAuthorizationCodeBearer
# import msal
# from src.core.config import get_app_settings, AppSettings, Settings
#
# app_settings: AppSettings = get_app_settings()
#
# azure_scheme = SingleTenantAzureAuthorizationCodeBearer(
#     app_client_id=app_settings.AppClientID,
#     tenant_id=app_settings.TenantID,
#     scopes={
#         f'api://{app_settings.AppClientID}/user_impersonation': 'user_impersonation'
#     }
# )
#
#
# @lru_cache
# def get_ms_app(settings: Settings) -> msal.ConfidentialClientApplication:
#     return msal.ConfidentialClientApplication(
#         settings.MSAppId,
#         authority=f"https://login.microsoftonline.com/{settings.TenantID}",
#         client_credential=settings.MSAppKey
#     )
#
#
# def get_ms_auth_token(settings: Settings):
#     ms_app = get_ms_app(settings)
#     result = ms_app.acquire_token_silent(["https://graph.microsoft.com/.default"], account=None)
#     if not result or result.get('error'):
#         result = ms_app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
#     return 'Bearer ' + result['access_token']
