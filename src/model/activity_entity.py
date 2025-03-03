from pydantic import BaseModel


class ActivityEntity(BaseModel):
    id: int
    activity: str