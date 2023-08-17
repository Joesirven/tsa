from pydantic import BaseModel
from queries.pool import pool
from decimal import Decimal
from datetime import date


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
  def create(self, transactions: TransactionsIn) -> TransactionsOut:
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