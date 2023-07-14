from mysql.connector import MySQLConnection

from src.model.plan_entity import PlanEntity


class PlanDao:
    __db: MySQLConnection

    def __init__(self, db: MySQLConnection):
        self.__db = db

    def fetch_all(self, date) -> list:
        cursor = self.__db.cursor()
        cursor.execute("SELECT id, for_day, id_horse, id_exercise, id_treatment FROM plan")

        db_results = cursor.fetchall()
        results = []

        for result in db_results:
            entity = PlanEntity(id=result[0], for_day=result[1], id_horse=result[2],
                                id_exercise=result[3], id_treatment=result[4])
            results.append(entity)

        return results

    def create_plan(self, id, date, horse_id, exercise_id, treatment_id) -> int:
        return 0

    def update_plan(self, id, what_to_update, new_value):
        return None

    def delete_plan(self, id):
        return None