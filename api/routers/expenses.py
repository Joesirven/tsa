from fastapi import APIRouter, Depends, Response
from typing import Union, List, Optional
from queries.expenses import Error, ExpenseIn, ExpenseOut, ExpenseRepository


router = APIRouter()


@router.post("/expense/create", response_model=Union[ExpenseOut, Error])
def create_expense(
    expense: ExpenseIn,
    response: Response,
    repo: ExpenseRepository = Depends()
):
    return repo.create(expense)


@router.get("/expense", response_model=Union[List[ExpenseOut], Error])
def get_all(
    repo: ExpenseRepository = Depends(),
):
    return repo.get_all()


@router.put("/expense/{expense_id}", response_model=Union[ExpenseOut, Error])
def update_expense(
    expense_id: int,
    expense: ExpenseIn,
    repo: ExpenseRepository = Depends(),
) -> Union[Error, ExpenseOut]:
    return repo.update(expense_id, expense)


@router.delete("/expense/{expense_id}", response_model=bool)
def delete_expense(
    expense_id: int,
    repo: ExpenseRepository = Depends(),
) -> bool:
    return repo.delete(expense_id)


@router.get("/expense/{expense_id}", response_model=Optional[ExpenseOut])
def get_one_expense(
    expense_id: int,
    response: Response,
    repo: ExpenseRepository = Depends(),
) -> ExpenseOut:
    expense = repo.get_one(expense_id)
    if expense is None:
        response.status_code = 404
    return expense
