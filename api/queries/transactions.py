from pydantic import BaseModel
from queries.pool import pool
from decimal import Decimal
from datetime import date
from typing import Union, List, Optional


class TransactionsIn(BaseModel):
  amount_saved: Decimal
  date: date


class TransactionsOut(BaseModel):
  id: int
  amount_saved: Decimal
  date: date

class Error(BaseModel):
  message: str


class TransactionsRepository:
  def get_one(self, transactions_id:int) -> Optional[TransactionsOut]:
      try:
        with pool.connection() as conn:
          with conn.cursor() as db:
            result = db.execute(
              """
                SELECT id, amount_saved, date
                FROM transactions
                WHERE id = %s
              """,
              [
                transactions_id
              ]
            )
            record = result.fetchone()
            if record is None:
              return None
            return self.record_to_transactions_out(record)
      except Exception as e:
        return {"message": e}


  def delete(self, transactions_id: int) -> bool:
    try:
      with pool.connection() as conn:
        with conn.cursor() as db:
          db.execute(
            """
            DELETE FROM transactions
            WHERE id = %s
            """,
            [transactions_id]
          )
          return True
    except Exception as e:
        return False


  def update(self, transactions_id:int, transactions: TransactionsIn) -> Union[TransactionsOut, Error]:
    try:
      with pool.connection() as conn:
        with conn.cursor() as db:
          db.execute(
            """
              UPDATE transactions
              SET amount_saved = %s,
                date = %s
              WHERE id = %s
            """,
            [
              transactions.amount_saved,
              transactions.date,
              transactions_id
            ]
          )
          return self.transactions_in_to_out(transactions_id, transactions)
    except Exception as e:
      return {"message": e}


  def get_all(self) -> Union[List[TransactionsOut], Error]:
    try:
      with pool.connection() as conn:
        with conn.cursor() as db:
          db.execute(
            """
              SELECT id, amount_saved, date
              FROM transactions;
            """
          )
          return [
            TransactionsOut(
              id=record[0],
              amount_saved=record[1],
              date=record[2]
            )
            for record in db
          ]
    except Exception as e:
      return {"message": e}


  def create(self, transactions: TransactionsIn) -> TransactionsOut:
    try:
      with pool.connection() as conn:
        with conn.cursor() as db:
          result = db.execute(
            """
            INSERT INTO transactions
              (
                amount_saved,
                date
              )
            VALUES
              (%s, %s)
            RETURNING id;
            """,
            [
              transactions.amount_saved,
              transactions.date
            ]
          )
          id = result.fetchone()[0]
          return self.transactions_in_to_out(id, transactions)
    except Exception as e:
      return {"message": e}

  def transactions_in_to_out(self, id: int, transactions: TransactionsIn):
    old_data = transactions.dict()
    return TransactionsOut(id=id, **old_data)

  def record_to_transactions_out(self, record):
    return TransactionsOut(
      id=record[0],
      amount_saved=record[1],
      date=record[2]
    )
