from beanie import Document, PydanticObjectId
from app.models.common import TimestampMixin


class GPS(Document, TimestampMixin):
    point: PydanticObjectId 
    point_gps_id: int | None = None
    lat: float
    lon: float
    speed: float

    class Settings:
        name = "gps_collection"
        validate_on_save = True

    class Config:
        schema_extra = {
            "example": {
                "point": "60f7a1f8d0a5d5b1d0b4c1a1",
                "lat": 43.222,
                "lon": 76.851,
                "speed": 60.0
            }
        }