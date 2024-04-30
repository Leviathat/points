from app.models.point import Point
from app.schemas.point import PointIn
from beanie import PydanticObjectId


class PointService:

    async def create_point(self, point: PointIn) -> Point:
        return await Point(**point.dict()).create()

    async def get_point(self, point_id: PydanticObjectId) -> list[Point]:
        return await Point.get(point_id)

    async def get_all_points(self) -> list[Point]:
        return await Point.find_all().to_list()

    
point_service = PointService()