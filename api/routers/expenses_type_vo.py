from fastapi import APIRouter, Depends, Response
from typing import Union, List
from queries.expenses_type_vo import Expense_type_voIn, Expense_type_voOut, Expense_type_voRepository, Error


router = APIRouter()


@router.post("/expense_type_vo/create", response_model=Union[Expense_type_voOut, Error])
def create_expense_type_vo(
    expense_type_vo: Expense_type_voIn,
    response: Response,
    repo: Expense_type_voRepository = Depends()
):
    response.status_code = 400
    return repo.create(expense_type_vo)


@router.get("/expense_type_vo", response_model=Union[List[Expense_type_voOut], Error])
def get_all(
    repo: Expense_type_voRepository = Depends(),
):
    return repo.get_all()


@router.put("/expense_type_vo/{expense_type_vo_id}", response_model=Union[Expense_type_voOut, Error])
def update_expense_type_vo(
    expense_type_vo_id: int,
    expense_type_vo: Expense_type_voIn,
    repo: Expense_type_voRepository = Depends(),
) -> Union[Error, Expense_type_voOut]:
    return repo.update(expense_type_vo_id, expense_type_vo)
