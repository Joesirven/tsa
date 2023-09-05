from pydantic import BaseModel
from queries.pool import pool
from decimal import Decimal
from datetime import date
from typing import Union, List, Optional


class TransactionsIn(BaseModel):
  amount_saved: Decimal
  date: date
  savings_id: int


class TransactionsOut(BaseModel):
  id: int
  amount_saved: Decimal
  date: date
  savings_id: int

class Error(BaseModel):
  message: str


class TransactionsRepository:
  def get_one(self, transactions_id:int) -> Optional[TransactionsOut]:
      try:
        with pool.connection() as conn:
          with conn.cursor() as db:
            result = db.execute(
              """
                SELECT id, savings_id, amount_saved, date
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
        print(e)
        return False


  def update(self, transactions_id:int, transactions: TransactionsIn) -> Union[TransactionsOut, Error]:
    try:
      with pool.connection() as conn:
        with conn.cursor() as db:
          db.execute(
            """
              UPDATE transactions
              SET savings_id = %s,
                amount_saved = %s,
                date = %s
              WHERE id = %s
            """,
            [
              transactions.savings_id,
              transactions.amount_saved,
              transactions.date,
              transactions_id
            ]
          )
          return self.transactions_in_to_out(transactions_id, transactions)
    except Exception as e:
      print(e)
      return {"message": e}


  def get_all(self) -> Union[List[TransactionsOut], Error]:
    try:
      with pool.connection() as conn:
        with conn.cursor() as db:
          db.execute(
            """
              SELECT id, savings_id, amount_saved, date
              FROM transactions;
            """
          )
          return [
            TransactionsOut(
              id=record[0],
              savings_id=record[1],
              amount_saved=record[2],
              date=record[3]
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
                date,
                savings_id
              )
            VALUES
              (%s, %s, %s)
            RETURNING id;
            """,
            [
              transactions.amount_saved,
              transactions.date,
              transactions.savings_id
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
      savings_id=record[1],
      amount_saved=record[2],
      date=record[3]
    )
