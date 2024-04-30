from pydantic import BaseModel
from beanie import PydanticObjectId


class GPSIn(BaseModel):
    point: PydanticObjectId
    lat: float
    lon: float
    speed: float


class GPSData(BaseModel):
    alias: str
    lat: float
    lon: float
    speed: float


class ParamsData(BaseModel):
    alias: str
    channel: int
    value: str