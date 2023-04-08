from fastapi import FastAPI
from app.main.config import Config
from app.main.feature.resource import feature_resource

fast_app = FastAPI(
    title="FastAPI Boilerplate",
    description="FastAPI Boilerplate Application",
    version=Config.get_application_version()
)

fast_app.include_router(
    feature_resource.feature_router, prefix="/api"
)