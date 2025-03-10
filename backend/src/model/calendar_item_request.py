import datetime
from pydantic import BaseModel
from typing import Optional


class CalendarItemRequest(BaseModel):
    id_activity: Optional[str]
    id_horse: int
    date: datetime.date # yyyy-mm-dd

