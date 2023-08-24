from fastapi import APIRouter, Depends, Response
from typing import Union, List, Optional
from queries.expenses import Error, ExpenseIn, ExpenseOut, ExpenseRepository
from authenticator import authenticator


router = APIRouter()


@router.post("/expense/create", response_model=Union[ExpenseOut, Error])
async def create_expense(
    expense: ExpenseIn,
    response: Response,
    repo: ExpenseRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
):
    return repo.create(expense)


@router.get("/expense", response_model=Union[List[ExpenseOut], Error])
async def get_all(
    repo: ExpenseRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
):
    return repo.get_all()


@router.put("/expense/{expense_id}", response_model=Union[ExpenseOut, Error])
async def update_expense(
    expense_id: int,
    expense: ExpenseIn,
    repo: ExpenseRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
) -> Union[Error, ExpenseOut]:
    return repo.update(expense_id, expense)


@router.delete("/expense/{expense_id}", response_model=bool)
async def delete_expense(
    expense_id: int,
    repo: ExpenseRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
) -> bool:
    return repo.delete(expense_id)


@router.get("/expense/{expense_id}", response_model=Optional[ExpenseOut])
async def get_one_expense(
    expense_id: int,
    response: Response,
    repo: ExpenseRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
) -> ExpenseOut:
    expense = repo.get_one(expense_id)
    if expense is None:
        response.status_code = 404
    return expense
