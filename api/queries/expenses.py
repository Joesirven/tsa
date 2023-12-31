from pydantic import BaseModel
from typing import List, Union, Optional
from queries.pool import pool
from decimal import Decimal


class Error(BaseModel):
    message: str


class ExpenseIn(BaseModel):
    name: str
    cost: Decimal
    paid: bool
    type: str
    plans_id: int


class ExpenseOut(BaseModel):
    id: int
    name: str
    cost: Decimal
    paid: bool
    type: str
    plans_id: int


class ExpenseRepository:
    def get_one(self, expense_id: int) -> Optional[ExpenseOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, name, cost, paid, type, plans_id
                        FROM expenses
                        WHERE id = %s
                        """,
                        [expense_id],
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return self.record_to_expense_out(record)
        except Exception as e:
            return {"message": "Could not get that expense"}

    def delete(self, expense_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM expenses
                        WHERE id = %s
                        """,
                        [expense_id],
                    )
                    return True
        except Exception as e:
            return False

    def update(
        self, expense_id: int, expense: ExpenseIn
    ) -> Union[ExpenseOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE expenses
                        SET name = %s,
                        cost = %s,
                        paid = %s,
                        type = %s,
                        plans_id = %s
                        WHERE id = %s
                        """,
                        [
                            expense.name,
                            expense.cost,
                            expense.paid,
                            expense.type,
                            expense.plans_id,
                            expense_id,
                        ],
                    )
                    return self.expense_in_to_out(expense_id, expense)
        except Exception as e:
            return {"message": "Could not update expense"}

    def get_all(self) -> Union[Error, List[ExpenseOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, name, cost, paid, type, plans_id
                        FROM expenses
                        ORDER BY type;
                        """
                    )
                    return [
                        self.record_to_expense_out(record) for record in result
                    ]
        except Exception as e:
            return {"message": "Could not get all expenses"}

    def create(self, expense: ExpenseIn) -> Union[ExpenseOut, Error]:
        try:
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
                            expense.type,
                        ],
                    )
                    id = result.fetchone()[0]
                    return self.expense_in_to_out(id, expense)
        except Exception as e:
            return {"message": "Could not create expense"}

    def expense_in_to_out(self, id: int, expense: ExpenseIn):
        old_data = expense.dict()
        return ExpenseOut(id=id, **old_data)

    def record_to_expense_out(self, record):
        return ExpenseOut(
            id=record[0],
            name=record[1],
            cost=record[2],
            paid=record[3],
            type=record[4],
            plans_id=record[5],
        )
