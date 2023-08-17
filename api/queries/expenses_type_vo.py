from pydantic import BaseModel
from queries.pool import pool
from decimal import Decimal


class Error(BaseModel):
    message: str


class Expense_type_voIn(BaseModel):
    name: str


class Expense_type_voOut(BaseModel):
    id: int
    name: str


class Expense_type_voRepository:
  def create(self, expense_type_vo: Expense_type_voIn) -> Expense_type_voOut:
    with pool.connection() as conn:
        with conn.cursor() as db:
            result = db.execute(
                """
                INSERT INTO expenses_type_vo
                    (
                    name
                    )
                VALUES
                    (%s)
                RETURNING id;
                """,
                [
                    expense_type_vo.name
                ]
            )
            id = result.fetchone()[0]
            old_data = expense_type_vo.dict()
            return Expense_type_voOut(id=id, **old_data)