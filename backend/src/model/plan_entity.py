import datetime
from typing import Optional

from pydantic import BaseModel


class PlanEntity(BaseModel):
    id: int
    for_day: datetime.date
    id_horse: int
    id_activity: Optional[str]
