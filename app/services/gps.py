from app.models.gps import GPS
from fastapi import HTTPException
from app.schemas.gps import GPSIn, GPSData
from beanie import PydanticObjectId
from app.models.point import Point
from app.models.params_string import ParamsString
from app.models.params_int import ParamsInt
from app.schemas.params_string import ParamsData

class GPSService:

    async def create_gps(self, gps: GPSIn) -> GPS:
        return await GPS(**gps.dict()).create()

    async def get_gps(self, gps_id: PydanticObjectId) -> list[GPS]:
        return await GPS.get(gps_id)

    async def get_all_gps(self) -> list[GPS]:
        return await GPS.find_all().to_list()

    async def create_gps_data(self, gps_data: GPSData) -> GPS:
        point = await Point.find_one(Point.alias == gps_data.alias)
        if not point:
            raise HTTPException(status_code=404, detail="Point not found")
        point_gps_id = await GPS.find_all(point).count()
        gps = await GPS(
            point=point.id,
            point_gps_id=point_gps_id,
            lat=gps_data.lat,
            lon=gps_data.lon,
            speed=gps_data.speed,
        ).insert()
        return gps
    
    async def add_params_data(params_data: ParamsData):
        point = await Point.find_one(Point.alias == params_data.alias)
        if not point:
            raise HTTPException(status_code=404, detail="Point not found")
        params = await ParamsString(
            point=point.id,
            channel=params_data.channel,
            value=params_data.value,
        ).insert()
        return params
    
    async def get_last_ids(alias, *args):
        point = await Point.find_one(Point.alias == args[0])
        if not point:
            raise HTTPException(status_code=404, detail="Point not found")
        query = {"point": point.id}
        last_gps_id = await GPS.find(query).sort(("time", -1)).limit(1).first_or_none()
        last_string_id = await ParamsString.find(query).sort(("time", -1)).limit(1).first_or_none()
        last_int_id = await ParamsInt.find(query).sort(("time", -1)).limit(1).first_or_none()
        result = {
            "last_gps_id": last_gps_id.id if last_gps_id else 0, 
            "last_string_id": last_string_id.id if last_string_id else 0, 
            "last_int_id": last_int_id.id if last_int_id else 0
            }
        return result
        
gps_service = GPSService()