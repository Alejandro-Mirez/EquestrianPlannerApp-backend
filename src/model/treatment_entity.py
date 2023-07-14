from pydantic import BaseModel


class TreatmentEntity(BaseModel):
    id: int
    treatment: str