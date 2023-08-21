from pydantic import BaseModel
from queries.pool import pool
from decimal import Decimal
from typing import List, Union


class Error(BaseModel):
    message: str


class Expense_type_voIn(BaseModel):
    name: str


class Expense_type_voOut(BaseModel):
    id: int
    name: str


class Expense_type_voRepository:
    def update(self, expense_type_vo_id: int, expense_type_vo: Expense_type_voIn) -> Union[Expense_type_voOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE expenses_type_vo
                        SET name = %s
                        WHERE id = %s
                        """,
                        [
                            expense_type_vo.name,
                            expense_type_vo_id
                        ]
                    )
                    return self.expense_type_vo_in_to_out(expense_type_vo_id, expense_type_vo)
        except Exception as e:
            print(e)
            return {"message": "Could not update expense_type_vo"}


    def get_all(self) -> Union[Error, List[Expense_type_voOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, name
                        FROM expenses_type_vo;
                        """
                    )
                    return [
                        Expense_type_voOut(
                            id=record[0],
                            name=record[1],
                        )
                        for record in db
                    ]
        except Exception as e:
            print(e)
            return {"message": "Could not get all expense_type_vos"}

    def create(self, expense_type_vo: Expense_type_voIn) -> Expense_type_voOut:
        try:
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
                    return self.expense_type_vo_in_to_out(id, expense_type_vo)
        except Exception as e:
            print(e)
            return {"message": "Could not create expense_type_vo"}

    def expense_type_vo_in_to_out(self, id: int, expense_type_vo: Expense_type_voIn):
        old_data = expense_type_vo.dict()
        return Expense_type_voOut(id=id, **old_data)
