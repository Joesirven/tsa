from fastapi import APIRouter, Depends
from queries.expenses_type_vo import Expense_type_voIn, Expense_type_voOut, Expense_type_voRepository


router = APIRouter()


@router.post("/expense_type_vo/create")
def create_expense_type_vo(
    expense_type_vo: Expense_type_voIn,
    repo: Expense_type_voRepository = Depends()
):
    return repo.create(expense_type_vo)
