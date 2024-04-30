from beanie import PydanticObjectId
from fastapi import APIRouter

from app.models.params_string import ParamsString
from app.schemas.params_string import ParamsStringIn

from app.services.gps import gps_service

router = APIRouter()

@router.post("/params_string", response_model=ParamsString)
async def create_params_string(params_string: ParamsStringIn):
    return await gps_service.create_gps(params_string)

@router.get("/params_string", response_model=list[ParamsString])
async def get_all_params_strings():
    return await gps_service.get_all_gps()

@router.get("/params_string/{params_string_id: str}", response_model=ParamsString)
async def get_params_string(params_string_id: PydanticObjectId):
    return await gps_service.get_gps(params_string_id)
