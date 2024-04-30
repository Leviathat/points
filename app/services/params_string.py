from app.models.params_string import ParamsString
from app.schemas.params_string import ParamsStringIn
from beanie import PydanticObjectId


class ParamsStringService:

    async def create_params_string(self, gps: ParamsStringIn) -> ParamsString:
        return await ParamsString(**gps.dict()).create()

    async def get_params_string(self, gps_id: PydanticObjectId) -> list[ParamsString]:
        return await ParamsString.get(gps_id)

    async def get_all_params_strings(self) -> list[ParamsString]:
        return await ParamsString.find_all().to_list()

    
params_string_service = ParamsStringService()