from pydantic import BaseModel
from queries.pool import pool
from datetime import date
from decimal import Decimal


class PlansIn(BaseModel):
  start_of_budget: date
  end_of_budget: date
  trip_start_date: date
  trip_end_date: date
  destination: str
  monthly_budget: Decimal


class PlansOut(BaseModel):
  id: int
  start_of_budget: date
  end_of_budget: date
  trip_start_date: date
  trip_end_date: date
  destination: str
  monthly_budget: Decimal
  

class PlansRepository:
  def create(self, plan: PlansIn) -> PlansOut:
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
        old_data = plan.dict()
        return PlansOut(id=id, **old_data)