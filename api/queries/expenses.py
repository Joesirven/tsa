from pydantic import BaseModel
from queries.pool import pool
from decimal import Decimal


class Error(BaseModel):
    message: str


class ExpenseIn(BaseModel):
    name: str
    cost: Decimal
    paid: bool
    type: str


class ExpenseOut(BaseModel):
    id: int
    name: str
    cost: Decimal
    paid: bool
    type: str  


class ExpenseRepository:
  def create(self, expense: ExpenseIn) -> ExpenseOut:
    with pool.connection() as conn:
        with conn.cursor() as db:
            result = db.execute(
                """
                INSERT INTO expenses
                    (
                    name,
                    cost,
                    paid,
                    type
                    )
                VALUES
                    (%s, %s, %s, %s)
                RETURNING id;
                """,
                [
                    expense.name,
                    expense.cost,
                    expense.paid,
                    expense.type
                ]
            )
            id = result.fetchone()[0]
            old_data = expense.dict()
            return {"message": "error!"}
            return ExpenseOut(id=id, **old_data)