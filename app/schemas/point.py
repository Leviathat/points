from pydantic import BaseModel

class PointIn(BaseModel):
    name: str
    alias: str
    password: str