from pydantic import BaseModel
from typing import List, Union, Optional
from queries.pool import pool
from datetime import date, timedelta
from decimal import Decimal
from authenticator import authenticator
from fastapi import Depends
from queries.savings import SavingsRepository, SavingsIn, SavingsOut
from queries.transactions import (
    TransactionsRepository,
    TransactionsIn,
    TransactionsOut,
)


class Error(BaseModel):
    message: str


class PlansIn(BaseModel):
    start_of_budget: date
    end_of_budget: date
    trip_start_date: date
    trip_end_date: date
    destination: str
    monthly_budget: Decimal
    users_id: int


class PlansOut(BaseModel):
    id: int
    start_of_budget: date
    end_of_budget: date
    trip_start_date: date
    trip_end_date: date
    destination: str
    monthly_budget: Decimal
    users_id: int


class PlansRepository:
    def get_one(self, plan_id: int) -> Optional[PlansOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
              SELECT id,
                start_of_budget,
                end_of_budget,
                trip_start_date,
                trip_end_date,
                destination,
                monthly_budget,
                users_id
              FROM plans
              WHERE id = %s
            """,
                        [plan_id],
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return self.record_to_plan_out(record)
        except Exception as e:
            return {"message": "could not get plan"}

    def delete(self, plan_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
            DELETE FROM plans
            WHERE id = %s
            """,
                        [plan_id],
                    )
                    return True
        except Exception as e:
            return False

    def update(self, plan_id: int, plan: PlansIn) -> Union[Error, PlansOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
            UPDATE plans

            SET start_of_budget = %s,
                end_of_budget = %s,
                trip_start_date = %s,
                trip_end_date = %s,
                destination = %s,
                monthly_budget = %s,
                users_id = %s
            WHERE id = %s
                """,
                        [
                            plan.start_of_budget,
                            plan.end_of_budget,
                            plan.trip_start_date,
                            plan.trip_end_date,
                            plan.destination,
                            plan.monthly_budget,
                            plan.users_id,
                            plan_id,
                        ],
                    )
                    return self.plan_in_to_out(plan_id, plan)
        except Exception as e:
            return {"message": "Could not get all plans."}

    def get_all(self) -> Union[Error, List[PlansOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
            SELECT id, start_of_budget, end_of_budget, trip_start_date, trip_end_date, destination, monthly_budget, users_id
            FROM plans
            ORDER BY trip_start_date;
            """
                    )
                    return [
                        PlansOut(
                            id=record[0],
                            start_of_budget=record[1],
                            end_of_budget=record[2],
                            trip_start_date=record[3],
                            trip_end_date=record[4],
                            destination=record[5],
                            monthly_budget=record[6],
                            users_id=record[7],
                        )
                        for record in db
                    ]
        except Exception as e:
            return {"message": "Could not get all plans."}

    def create(self, plan: PlansIn) -> Union[PlansOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
            INSERT INTO plans
              (
              start_of_budget,
              end_of_budget,
              trip_start_date,
              trip_end_date,
              destination,
              monthly_budget,
              users_id
              )
            VALUES
              (%s, %s, %s, %s, %s, %s, %s)
            RETURNING id;
            """,
                        [
                            plan.start_of_budget,
                            plan.end_of_budget,
                            plan.trip_start_date,
                            plan.trip_end_date,
                            plan.destination,
                            plan.monthly_budget,
                            plan.users_id,
                        ],
                    )
                    id = result.fetchone()[0]
                    return self.plan_in_to_out(id, plan)
        except Exception as e:
            return {"message": "Could not create plan."}

    def plan_in_to_out(self, id: int, plan: PlansIn):
        old_data = plan.dict()
        return PlansOut(id=id, **old_data)

    def record_to_plan_out(self, record):
        return PlansOut(
            id=record[0],
            start_of_budget=record[1],
            end_of_budget=record[2],
            trip_start_date=record[3],
            trip_end_date=record[4],
            destination=str(record[5]),
            monthly_budget=Decimal(record[6]),
            users_id=record[7],
        )
