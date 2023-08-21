from pydantic import BaseModel
from queries.pool import pool
from decimal import Decimal
from typing import List, Union


class SavingsIn(BaseModel):
  current_amount_saved: Decimal
  final_goal_amount: Decimal
  if_saved: bool


class SavingsOut(BaseModel):
  id: int
  current_amount_saved: Decimal
  final_goal_amount: Decimal
  if_saved: bool


class Error(BaseModel):
  message: str


class SavingsRepository:
  def get_all(self) -> Union[Error, List[SavingsOut]]:
    try:
      #connect the databse
      with pool.connection() as conn:
        #get a cursor (something to run SQL with)
        with conn.cursor() as db:
        # Run our SELECT statement
          result = db.execute(
            """
              SELECT id, current_amount_saved, final_goal_amount, if_saved
              FROM savings
            """
          )
          return [
            SavingsOut(
              id=record[0],
              current_amount_saved=record[1],
              final_goal_amount=record[2],
              if_saved=record[3]
            )
            for record in db
          ]
    except Exception as e:
      return {"message": e}


  def create(self, savings: SavingsIn) -> SavingsOut:
    try:
      #connect the databse
      with pool.connection() as conn:
        #get a cursor (something to run SQL with)
        with conn.cursor() as db:
          # Run our INSERT statement
          result = db.execute(
            """
            INSERT INTO savings
              (
                current_amount_saved,
                final_goal_amount,
                if_saved
              )
            VALUES
              (%s, %s, %s)
            RETURNING id;
            """,
            [
            savings.current_amount_saved,
            savings.final_goal_amount,
            savings.if_saved
            ]
          )
          id = result.fetchone()[0]
          old_data = savings.dict()
          return SavingsOut(id=id, **old_data)
    except Exception as e:
      return {"message": e}
