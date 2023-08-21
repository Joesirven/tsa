from pydantic import BaseModel
from typing import List, Union
from queries.pool import pool
from datetime import date
from decimal import Decimal

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
  def update(self, plan_id: int, plan: PlansIn) -> Union[Error, PlansOut]:
    try:
      #connect the databse
      with pool.connection() as conn:
        #get a cursor (something to run SQL with)
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
              ]
          )
          # old_data = plan.dict()
          # return PlansOut(id=plan_id, **old_data)
          return self.plan_in_to_out(plan_id, plan)
    except Exception as e:
      print(e)
      return {"message": "Could not get all plans."}



  def get_all(self) -> Union[Error, List[PlansOut]]:
    try:
      #connect the databse
      with pool.connection() as conn:
        #get a cursor (something to run SQL with)
        with conn.cursor() as db:
        #Run our SELECT statement
          result =  db.execute(
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
      print(e)
      return {"message": "Could not get all plans."}

  def create(self, plan: PlansIn) -> PlansOut:
    try:
      #connect the databse
      with pool.connection() as conn:
        #get a cursor (something to run SQL with)
        with conn.cursor() as db:
        # Run our INSERT statement
          result = db.execute(
            """
            INSERT INTO plans
              (
              start_of_budget,
              end_of_budget,
              trip_start_date,
              trip_end_date,
              destination,
              monthly_budget
              )
            VALUES
              (%s, %s, %s, %s, %s, %s)
            RETURNING id;
            """,
            [
            plan.start_of_budget,
            plan.end_of_budget,
            plan.trip_start_date,
            plan.trip_end_date,
            plan.destination,
            plan.monthly_budget,
            ]
          )
          id = result.fetchone()[0]
          # old_data = plan.dict()
          # return PlansOut(id=id, **old_data)
          return self.plan_in_to_out(id, plan)
    except Exception as e:
      print(e)
      return {"message": "Could not create plan."}

  def plan_in_to_out(self, id: int, plan: PlansIn):
    old_data = plan.dict()
    return PlansOut(id=id, **old_data)
