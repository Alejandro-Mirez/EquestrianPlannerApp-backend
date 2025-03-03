from mysql.connector import MySQLConnection

from src.model.plan_entity import PlanEntity


class PlanDao:
    __db: MySQLConnection

    def __init__(self, db: MySQLConnection):
        self.__db = db

    def fetch_all(self, date) -> list[PlanEntity]:
        cursor = self.__db.cursor()
        cursor.execute("SELECT id, for_day, id_horse, id_activity FROM plan WHERE for_day = (%s)", (date,))

        db_results = cursor.fetchall()
        results = []

        for result in db_results:
            entity = PlanEntity(id=result[0], for_day=result[1], id_horse=result[2],
                                id_activity=result[3])
            results.append(entity)

        return results

    def create_plan(self, activity_id, horse_id, date) -> int:
        cursor = self.__db.cursor()
        cursor.execute("INSERT INTO plan (for_day, id_horse, id_activity) VALUES (%s, %s, %s)", (date, horse_id, activity_id))

        self.__db.commit()
        result = cursor.lastrowid
        return result

    def update_plan(self, val_id, activity_id):

        cursor = self.__db.cursor()
        cursor.execute("UPDATE plan SET id_activity = %s WHERE id = %s",
                    (activity_id, val_id))

        self.__db.commit()

    def delete_plan(self, val_id):
        cursor = self.__db.cursor()
        cursor.execute("DELETE FROM plan WHERE id = %s", (val_id,))
        self.__db.commit()