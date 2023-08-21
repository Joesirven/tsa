from fastapi import APIRouter, Depends, Response
from typing import Union, List
from queries.savings import SavingsIn, SavingsRepository, SavingsOut, Error


router = APIRouter()


@router.post("/savings/create", response_model=Union[SavingsOut, Error])
def create_savings(
  savings: SavingsIn,
  response: Response,
  repo: SavingsRepository = Depends()
):
    response.status_code = 400
    return repo.create(savings)


@router.get("/savings", response_model=Union[Error, List[SavingsOut]])
def get_all(
  repo: SavingsRepository = Depends(),
):
  return repo.get_all()
