from mysql.connector import MySQLConnection
from src.model.exercise_entity import ExerciseEntity


class ExerciseDao:
    __db: MySQLConnection

    def __init__(self, db: MySQLConnection):
        self.__db = db

    def fetch_all(self) -> list[ExerciseEntity]:
        cursor = self.__db.cursor()
        cursor.execute("SELECT id, exercise FROM exercise")

        db_results = cursor.fetchall()
        results = []

        for result in db_results:
            entity = ExerciseEntity(id=result[0], exercise=result[1])
            results.append(entity)

        return results
