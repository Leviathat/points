from pydantic import BaseModel
from beanie import PydanticObjectId

class ParamsStringIn(BaseModel):
    point: PydanticObjectId
    channel: int
    value: str

class ParamsData(BaseModel):
    alias: str
    channel: int
    value: str

