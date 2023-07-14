from pydantic import BaseModel


class HorseRequest(BaseModel):
    name: str

