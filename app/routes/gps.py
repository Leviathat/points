from beanie import PydanticObjectId
from fastapi import APIRouter

from app.models.gps import GPS
from app.schemas.gps import GPSIn, GPSData
from app.models.params_string import ParamsString
from app.schemas.params_string import ParamsData

from app.services.gps import gps_service

router = APIRouter()

@router.post("/gps", response_model=GPS)
async def create_gps(point: GPSIn):
    return await gps_service.create_gps(point)

@router.get("/gps", response_model=list[GPS])
async def get_all_gps():
    return await gps_service.get_all_gps()

@router.get("/gps/{gps_id: str}", response_model=GPS)
async def get_gps(gps_id: PydanticObjectId):
    return await gps_service.get_gps(gps_id)

@router.post("/gps_data", response_model=GPS)
async def create_gps_data(gps_data: GPSData):
    return await gps_service.create_gps_data(gps_data)

@router.get("/params_data", response_model=ParamsString)
async def add_params_data(params_data: ParamsData):
    return await gps_service.add_params_data(params_data)

@router.get("/last_ids/{alias: str}")
async def get_last_ids(alias: str):
    return await gps_service.get_last_ids(alias)