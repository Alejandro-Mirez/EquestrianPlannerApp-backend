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

    def create_horse(self, horse_name: str) -> int:
        cursor = self.__db.cursor()
        cursor.execute("INSERT INTO horse (name) VALUES (%s)", (horse_name,))
        self.__db.commit()
        result = cursor.lastrowid
        return result

    def update_horse(self, val_id, new_name: str):
        cursor = self.__db.cursor()
        cursor.execute("UPDATE horse SET name = %s WHERE id = %s", (new_name, val_id))
        self.__db.commit()

    def delete_horse(self, val_id):
        cursor = self.__db.cursor()
        cursor.execute("DELETE FROM horse WHERE id = %s", (val_id,))
        self.__db.commit()
