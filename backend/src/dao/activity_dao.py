# dao = Data Access Object

from mysql.connector import MySQLConnection
from src.model.activity_entity import ActivityEntity


class ActivityDao:
    __db: MySQLConnection

    def __init__(self, db: MySQLConnection):
        self.__db = db

    def fetch_all(self) -> list[ActivityEntity]:
        cursor = self.__db.cursor()
        cursor.execute("SELECT id, activity FROM activity")

        db_results = cursor.fetchall()
        results = []

        for result in db_results:
            entity = ActivityEntity(id=result[0], activity=result[1])
            results.append(entity)

        return results
