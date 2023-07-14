import datetime
from pydantic import BaseModel


class CalendarItemRequest(BaseModel):
    category: str
    activity: str
    horse_id: int
    date: datetime.date
