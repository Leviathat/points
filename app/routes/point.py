from beanie import PydanticObjectId
from fastapi import APIRouter

from app.models.point import Point
from app.schemas.point import PointIn

from app.services.point import point_service

router = APIRouter()

@router.post("/point", response_model=Point)
async def create_point(point: PointIn):
    return await point_service.create_point(point)

@router.get("/point", response_model=list[Point])
async def get_all_points():
    return await point_service.get_all_points()

@router.get("/point/{point_id: str}", response_model=Point)
async def get_point(point_id: PydanticObjectId):
    return await point_service.get_point(point_id)
