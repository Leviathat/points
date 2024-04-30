from beanie import Document, PydanticObjectId
from app.models.common import TimestampMixin


class ParamsInt(Document, TimestampMixin):
    point: PydanticObjectId
    channel: int
    value: str


    class Settings:
        name = "params_int_collection"
        validate_on_save = True

    class Config:
        schema_extra = {
            "example": {
                "point": "60f7a1f8d0a5d5b1d0b4c1a1",
                "channel": 1,
                "value": "value"
            }
        }