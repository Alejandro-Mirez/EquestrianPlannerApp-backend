from pydantic import BaseModel


class ExerciseEntity(BaseModel):
    id: int
    exercise: str