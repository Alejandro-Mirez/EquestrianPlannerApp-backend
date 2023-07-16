import datetime
from fastapi import FastAPI
import mysql.connector

from src.dao.exercise_dao import ExerciseDao
from src.dao.horse_dao import HorseDao
from src.dao.plan_dao import PlanDao
from src.dao.treatment_dao import TreatmentDao
from src.model.calendar_item_request import CalendarItemRequest
from src.model.calendar_item_update import CalendarItemUpdate
from src.model.horse_request import HorseRequest

app = FastAPI()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Firisacce324b21:",
    database="eep"
)

treatment_dao = TreatmentDao(db)
exercise_dao = ExerciseDao(db)
horse_dao = HorseDao(db)
plan_dao = PlanDao(db)

@app.get("/health")
async def health():
    return {}


@app.get("/horses")
async def get_horses():
    return horse_dao.fetch_all()


@app.post("/horse")
async def add_horse(horse: HorseRequest):
    return horse_dao.create_horse(horse.name)


@app.delete("/horse/{id}")
async def delete_horse(id):
    return horse_dao.delete_horse(id)


@app.put("/horse/{id}")
async def update_horse(id, horse: HorseRequest):
    return horse_dao.update_horse(id, horse.name)


@app.get("/calendar")
async def get_calendar(date: datetime.date):
    return plan_dao.fetch_all(date)


@app.post("/calendar/item")
async def add_to_calendar(item: CalendarItemRequest):
    if item.exercise_id is None and item.treatment_id is None:
        raise ValueError("You must provide either exercise_id or treatment_id (or both) to create a plan")

    return plan_dao.create_plan(item.exercise_id, item.treatment_id, item.horse_id, item.date)


@app.delete("/calendar/item/{id}")
async def delete_activity(id):
    return plan_dao.delete_plan(id)


@app.put("/calendar/item/{id}")
async def update_activity(id, item: CalendarItemUpdate):
    if item.exercise_id is None and item.treatment_id is None:
        raise ValueError("You must provide either exercise_id or treatment_id (or both) to update a plan")

    return plan_dao.update_plan(id, item.exercise_id, item.treatment_id)

@app.get("/exercises")
async def get_exercises():
    return exercise_dao.fetch_all()

@app.get("/treatments")
async def get_treatments():
    return treatment_dao.fetch_all()

@app.on_event("shutdown")
def shutdown_event():
    db.close()