
from pydantic import BaseModel
from typing import Optional


class CalendarItemUpdate(BaseModel):
    exercise_id: Optional[int]
    treatment_id: Optional[int]
