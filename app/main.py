from fastapi import FastAPI

from app.routers.v1 import api
from app.resources.data import src
from app.core.settings import settings
from app.logger.logger import logger


app = FastAPI(title=settings.app_name)
app.include_router(api.router)


@app.on_event("startup")
async def startup_event():
    logger.info("Reading resources")
    await src.get_data_tasks()
    await src.get_data_builds()
