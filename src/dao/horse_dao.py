# horse database access object

from mysql.connector import MySQLConnection

from src.model.horse_entity import HorseEntity


class HorseDao:
    __db: MySQLConnection

    def __init__(self, db: MySQLConnection):
        self.__db = db

    def fetch_all(self) -> list:
        cursor = self.__db.cursor()
        cursor.execute("SELECT id, name FROM horse")

        db_results = cursor.fetchall()
        results = []

        for result in db_results:
            entity = HorseEntity(id=result[0], name=result[1])
            results.append(entity)

        return results

    def create_horse(self, name: str) -> int:
        return 0

    def update_horse(self, id, name: str):
        return None

    def delete_horse(self, id):
        return None