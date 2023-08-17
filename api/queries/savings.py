from pydantic import BaseModel
from queries.pool import pool
from decimal import Decimal


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
  def create(self, savings: SavingsIn) -> SavingsOut:
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