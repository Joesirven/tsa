from pydantic import BaseModel
from queries.pool import pool
from decimal import Decimal
from typing import List, Union, Optional


class SavingsIn(BaseModel):
  current_amount_saved: Decimal
  final_goal_amount: Decimal
  plans_id: int


class SavingsOut(BaseModel):
  id: int
  current_amount_saved: Decimal
  final_goal_amount: Decimal
  plans_id: int


class Error(BaseModel):
  message: str


class SavingsRepository:
  def get_one(self, savings_id:int) -> Optional[SavingsOut]:
    try:
      with pool.connection() as conn:
        with conn.cursor() as db:
          result = db.execute(
            """
              SELECT id, plans_id, current_amount_saved, final_goal_amount
              FROM savings
              WHERE id = %s
            """,
            [
              savings_id
            ]
          )
          record = result.fetchone()
          if record is None:
            return None
          return self.record_to_savings_out(record)
    except Exception as e:
      print(e)
      return {"message": e}


  def delete(self, savings_id: int) -> bool:
    try:
      with pool.connection() as conn:
        with conn.cursor() as db:
          db.execute(
            """
            DELETE FROM savings
            WHERE id = %s
            """,
            [savings_id]
          )
          return True
    except Exception as e:
        print(e)
        return False


  def update(self, savings_id:int, savings: SavingsIn) -> Union[SavingsOut, Error]:
    try:
      with pool.connection() as conn:
        with conn.cursor() as db:
          db.execute(
            """
              UPDATE savings
              SET plans_id = %s,
                  current_amount_saved = %s,
                  final_goal_amount = %s
              WHERE id = %s
            """,
            [
              savings.plans_id,
              savings.current_amount_saved,
              savings.final_goal_amount,
              savings_id
            ]
          )
          return self.savings_in_to_out(savings_id, savings)
    except Exception as e:
      return {"message": e}

  def get_all(self) -> Union[Error, List[SavingsOut]]:
    try:
      with pool.connection() as conn:
        with conn.cursor() as db:
          db.execute(
            """
              SELECT id, plans_id, current_amount_saved, final_goal_amount
              FROM savings
            """
          )
          return [
            SavingsOut(
              id=record[0],
              plans_id=record[1],
              current_amount_saved=record[2],
              final_goal_amount=record[3]
            )
            for record in db
          ]
    except Exception as e:
      return {"message": e}


  def create(self, savings: SavingsIn) -> SavingsOut:
    try:
      with pool.connection() as conn:
        with conn.cursor() as db:
          result = db.execute(
            """
            INSERT INTO savings
              (
                plans_id,
                current_amount_saved,
                final_goal_amount
              )
            VALUES
              (%s, %s, %s)
            RETURNING id;
            """,
            [
            savings.plans_id,
            savings.current_amount_saved,
            savings.final_goal_amount
            ]
          )
          id = result.fetchone()[0]
          return self.savings_in_to_out(id, savings)
    except Exception as e:
      print(e)
      return {"message": e}


  def savings_in_to_out(self, id:int, savings: SavingsIn):
    old_data = savings.dict()
    return SavingsOut(id=id, **old_data)

  def record_to_savings_out(self, record):
    return SavingsOut(
      id=record[0],
      plans_id=record[1],
      current_amount_saved=record[2],
      final_goal_amount=record[3]
    )
