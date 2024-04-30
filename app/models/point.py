from beanie import Document


class Point(Document):
    name: str
    alias: str 
    password: str 

    class Settings:
        name = "points_collection"
        validate_on_save = True

    class Config:
        schema_extra = {
            "example": {
                "name": "name",
                "alias": "alias",
                "password": "password"
            }
        }
