from mysql.connector import MySQLConnection

from src.model.plan_entity import PlanEntity


class PlanDao:
    __db: MySQLConnection

    def __init__(self, db: MySQLConnection):
        self.__db = db

    def fetch_all(self, date) -> list:
        cursor = self.__db.cursor()
        cursor.execute("SELECT id, for_day, id_horse, id_exercise, id_treatment FROM plan WHERE for_day = (%s)", (date,))

        db_results = cursor.fetchall()
        results = []

        for result in db_results:
            entity = PlanEntity(id=result[0], for_day=result[1], id_horse=result[2],
                                id_exercise=result[3], id_treatment=result[4])
            results.append(entity)

        return results

    def create_plan(self, exercise_id, treatment_id, horse_id, date) -> int:
        cursor = self.__db.cursor()
        cursor.execute("INSERT INTO plan (for_day, id_horse, id_exercise, id_treatment) VALUES (%s, %s, %s, %s)", (date, horse_id, exercise_id, treatment_id))

        self.__db.commit()
        result = cursor.lastrowid
        return result

    def update_plan(self, val_id, exercise_id, treatment_id):

        cursor = self.__db.cursor()
        cursor.execute("UPDATE plan SET id_exercise = %s, id_treatment = %s WHERE id = %s",
                    (exercise_id, treatment_id, val_id))

        self.__db.commit()

    def delete_plan(self, val_id):
        cursor = self.__db.cursor()
        cursor.execute("DELETE FROM plan WHERE id = %s", (val_id,))
        self.__db.commit()