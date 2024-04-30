from beanie import PydanticObjectId
from fastapi import APIRouter

from app.models.params_int import ParamsInt
from app.schemas.params_int import ParamsIntIn

from app.services.params_int import params_int_service

router = APIRouter()

@router.post("/params_int", response_model=ParamsInt)
async def create_params_int(params_int: ParamsIntIn):
    return await params_int_service.create_params_int(params_int)

@router.get("/params_int", response_model=list[ParamsInt])
async def get_all_params_ints():
    return await params_int_service.get_all_params_int()

@router.get("/params_int/{params_int_id: str}", response_model=ParamsInt)
async def get_params_int(params_int_id: PydanticObjectId):
    return await params_int_service.get_params_int(params_int_id)
