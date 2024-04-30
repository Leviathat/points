from datetime import datetime, timedelta
from typing import List
from enum import Enum
from beanie import Document
from pydantic import BaseModel, EmailStr
import pytz


class TimestampMixin(BaseModel):
    time: datetime = datetime.now(pytz.timezone('Asia/Almaty'))
