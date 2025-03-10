
from pydantic import BaseModel
from typing import Optional


class CalendarItemUpdate(BaseModel):
    id_activity: Optional[int]
