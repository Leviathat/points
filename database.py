import motor.motor_asyncio
from beanie import init_beanie
from decouple import config

from app.models.point import Point
from app.models.params_int import ParamsInt
from app.models.params_string import ParamsString
from app.models.gps import GPS

MONGO_DETAILS = config("MONGO_DETAILS")

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
    document_models = [Point, ParamsInt, ParamsString, GPS]

    await init_beanie(
        database=client.point,
        document_models=document_models
    )
