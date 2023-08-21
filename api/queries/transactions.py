from pydantic import BaseModel
from queries.pool import pool
from decimal import Decimal
from datetime import date
from typing import Union, List


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
  def get_all(self) -> Union[Error, List[TransactionsOut]]:
    try:
      #connect the databse
      with pool.connection() as conn:
        #get a cursor (something to run SQL with)
        with conn.cursor() as db:
          # Run our SELECT statement
          result = db.execute(
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
      #connect the databse
      with pool.connection() as conn:
        #get a cursor (something to run SQL with)
        with conn.cursor() as db:
          # Run our INSERT statement
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
          old_data = transactions.dict()
          return TransactionsOut(id=id, **old_data)
    except Exception as e:
      return {"message": e}
