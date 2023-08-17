from fastapi import APIRouter, Depends, Response
from typing import Union
from queries.savings import SavingsIn, SavingsRepository, SavingsOut, Error


router = APIRouter()


@router.post("/savings/create", response_model = Union[SavingsOut, Error])
def create_savings(
  savings: SavingsIn,
  response: Response,
  repo: SavingsRepository = Depends()
):  
    response.status_code = 400
    return repo.create(savings)