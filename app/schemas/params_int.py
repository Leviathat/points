from pydantic import BaseModel
from beanie import PydanticObjectId

class ParamsIntIn(BaseModel):
    point: PydanticObjectId
    channel: int
    value: str

