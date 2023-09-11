from fastapi import APIRouter, Depends, Response
from typing import Union, List, Optional
from queries.expenses_type_vo import (
    Expense_type_voIn,
    Expense_type_voOut,
    Expense_type_voRepository,
    Error,
)
from authenticator import authenticator


router = APIRouter()


@router.post(
    "/expense_type_vo/create", response_model=Union[Expense_type_voOut, Error]
)
async def create_expense_type_vo(
    expense_type_vo: Expense_type_voIn,
    response: Response,
    repo: Expense_type_voRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
):
    return repo.create(expense_type_vo)


@router.get(
    "/expense_type_vo", response_model=Union[List[Expense_type_voOut], Error]
)
async def get_all(
    repo: Expense_type_voRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
):
    return repo.get_all()


@router.put(
    "/expense_type_vo/{expense_type_vo_id}",
    response_model=Union[Expense_type_voOut, Error],
)
async def update_expense_type_vo(
    expense_type_vo_id: int,
    expense_type_vo: Expense_type_voIn,
    repo: Expense_type_voRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
) -> Union[Error, Expense_type_voOut]:
    return repo.update(expense_type_vo_id, expense_type_vo)


@router.delete("/expense_type_vo/{expense_type_vo_id}", response_model=bool)
async def delete_expense(
    expense_type_vo_id: int,
    repo: Expense_type_voRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
) -> bool:
    return repo.delete(expense_type_vo_id)


@router.get(
    "/expense_type_vo/{expense_type_vo_id}",
    response_model=Optional[Expense_type_voOut],
)
async def get_one_expense_type_vo(
    expense_type_vo_id: int,
    response: Response,
    repo: Expense_type_voRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
) -> Expense_type_voOut:
    expense_type_vo = repo.get_one(expense_type_vo_id)
    if expense_type_vo is None:
        response.status_code = 404
    return expense_type_vo
