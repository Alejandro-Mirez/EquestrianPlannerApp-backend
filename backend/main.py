import datetime
from fastapi import FastAPI
import mysql.connector
from starlette.middleware.cors import CORSMiddleware

from src.dao.activity_dao import ActivityDao
from src.dao.horse_dao import HorseDao
from src.dao.plan_dao import PlanDao
from src.model.calendar_item_request import CalendarItemRequest
from src.model.calendar_item_update import CalendarItemUpdate
from src.model.horse_request import HorseRequest
from src.model.plan_entity import PlanEntity


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="eep"
)

activity_dao = ActivityDao(db)
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
async def get_calendar(date: datetime.date) -> list[PlanEntity]:
    return plan_dao.fetch_all(date)


@app.post("/calendar/item")
async def add_to_calendar(item: CalendarItemRequest):
    if item.id_activity is None:
        raise ValueError("You must provide activity id to create a plan")

    return plan_dao.create_plan(item.id_activity, item.id_horse, item.date)


@app.delete("/calendar/item/{id}")
async def delete_activity(id):
    return plan_dao.delete_plan(id)


@app.put("/calendar/item/{id}")
async def update_activity(id, item: CalendarItemUpdate):
    if item.id_activity is None:
        raise ValueError("You must provide activity id to update a plan")

    return plan_dao.update_plan(id, item.id_activity)


@app.get("/activities")
async def get_activities():
    return activity_dao.fetch_all()


@app.on_event("shutdown")
def shutdown_event():
    db.close()
