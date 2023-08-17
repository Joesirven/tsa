from fastapi import APIRouter, Depends, Response
from typing import Union
from queries.expenses import Error, ExpenseIn, ExpenseOut, ExpenseRepository


router = APIRouter()


@router.post("/expense/create", response_model=Union[ExpenseOut, Error])
def create_expense(
    expense: ExpenseIn,
    response: Response,
    repo: ExpenseRepository = Depends()
):
    response.status_code = 400
    return repo.create(expense)
