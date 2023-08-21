from fastapi import APIRouter, Depends, Response
from typing import Union, List
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


@router.get("/expense", response_model=Union[List[ExpenseOut], Error])
def get_all(
    repo: ExpenseRepository = Depends(),
):
    return repo.get_all()


# @router.put("/expense/{expenses_id}", response_model=Union[ExpenseOut, Error])
# def update_expense(
#     expenses_id: int,
#     expense: ExpenseIn,
#     repo: ExpenseRepository = Depends(),
# ) -> Union[Error, ExpenseOut]:
#     return repo.update(expenses_id, expense)
