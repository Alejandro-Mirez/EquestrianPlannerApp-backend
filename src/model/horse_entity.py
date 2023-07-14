from pydantic import BaseModel


class HorseEntity(BaseModel):
    id: int
    name: str
