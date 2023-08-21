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
