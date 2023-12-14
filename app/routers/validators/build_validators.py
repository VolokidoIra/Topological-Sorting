from fastapi import HTTPException, status

from app.resources.data import src


async def request_validators(request: dict) -> None:
    build_name = request.get('build', '')

    if not await check_request(request):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail='Empty request'
                            )
    if not await check_build_name_exist(build_name):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Empty build name'
                            )
    if not await check_build_name(build_name):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='The build name must be a string'
                            )
    if not await check_build_exist(build_name):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Build was not found'
                            )


async def check_request(request) -> bool:
    if not request:
        return False
    return True


async def check_build_name_exist(build_name) -> bool:
    if not build_name:
        return False
    return True


async def check_build_name(build_name) -> bool:
    if not isinstance(build_name, str):
        return False
    return True


async def check_build_exist(build_name) -> bool:
    if not src.builds.get(build_name):
        return False
    return True
