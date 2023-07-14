import datetime
from fastapi import FastAPI
import mysql.connector

from src.dao.treatment_dao import TreatmentDao
from src.model.calendar_item_request import CalendarItemRequest
from src.model.horse_request import HorseRequest

app = FastAPI()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Firisacce324b21:",
    database="eep"
)

treatment_dao = TreatmentDao(db)

@app.get("/health")
async def health():
    return {}


@app.get("/horses")
async def get_horses():
    return []


@app.post("/horse")
async def add_horse(horse: HorseRequest):
    return horse


@app.delete("/horse/{id}")
async def delete_horse(id):
    return id


@app.put("/horse/{id}")
async def update_horse(id, horse: HorseRequest):
    return horse


@app.get("/calendar")
async def get_calendar(date: datetime.date):
    return []


@app.post("/calendar/item")
async def add_to_calendar(item: CalendarItemRequest):
    return item


@app.delete("/calendar/item/{id}")
async def delete_activity(id):
    return id


@app.put("/calendar/item/{id}")
async def update_activity(id, item: CalendarItemRequest):
    return item

@app.get("/exercises")
async def get_exercises():
    return []

@app.get("/treatments")  #controller
async def get_treatments():
    return treatment_dao.fetch_all()

@app.on_event("shutdown")
def shutdown_event():
    db.close()