from app.models.params_int import ParamsInt
from app.schemas.params_int import ParamsIntIn
from beanie import PydanticObjectId


class ParamsIntService:

    async def create_params_int(self, params_int: ParamsIntIn) -> ParamsInt:
        return await ParamsInt(**params_int.dict()).create()

    async def get_params_int(self, params_int_id: PydanticObjectId) -> list[ParamsInt]:
        return await ParamsInt.get(params_int_id)

    async def get_all_params_int(self) -> list[ParamsInt]:
        return await ParamsInt.find_all().to_list()

    
params_int_service = ParamsIntService()