from fastapi import APIRouter, status, HTTPException

from app.schemas.build import Build
from app.services.topological_sort import get_tasks_order
from app.routers.validators.build_validators import request_validators
from app.logger.logger import logger

router = APIRouter()


@router.post("/get_tasks", status_code=200)
async def get_tasks_by_build(request: Build):
    logger.info(f"Request received\n{request}")

    request = request.model_dump()

    await request_validators(request)
    logger.success("Validation was successful")

    build_name = request.get('build')
    try:
        result: list = await get_tasks_order(build_name)

    except Exception as e:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                             detail=str(e)
                             )
    logger.success("Completed")

    return result
