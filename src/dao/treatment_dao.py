from mysql.connector import MySQLConnection
from src.model.treatment_entity import TreatmentEntity


class TreatmentDao:
    __db: MySQLConnection

    def __init__(self, db: MySQLConnection):
        self.__db = db

    def fetch_all(self) -> list[TreatmentEntity]:
        cursor = self.__db.cursor()
        cursor.execute("SELECT id, treatment FROM treatment")

        db_results = cursor.fetchall()
        # return map(lambda result: TreatmentEntity(id=result[0], treatment=result[1]),db_results)
        results = [] #lista obiektów (TreatmentEntity)

        for result in db_results:
            entity = TreatmentEntity(id=result[0], treatment=result[1])
            results.append(entity)

        return results
