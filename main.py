from fastapi import FastAPI

from app.routes.point import router as point_router
from app.routes.gps import router as gps_router
from app.routes.params_int import router as params_int_router
from app.routes.params_string import router as params_string_router


from database import init_db

app = FastAPI()

app.include_router(point_router, tags=["point"])
app.include_router(gps_router, tags=["gps"])
app.include_router(params_int_router, tags=["params_int"])
app.include_router(params_string_router, tags=["params_string"])



@app.on_event("startup")
async def start_db():
    await init_db()