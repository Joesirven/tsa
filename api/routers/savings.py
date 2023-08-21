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
    return repo.create(savings)


@router.get("/savings", response_model=Union[List[SavingsOut], Error])
def get_all(
  repo: SavingsRepository = Depends(),
):
  return repo.get_all()


@router.put("/savings/{savings_id}", response_model=Union[SavingsOut, Error])
def update_savings(
  savings_id: int,
  savings: SavingsIn,
  repo: SavingsRepository = Depends(),
) -> Union[Error, SavingsOut]:
  return repo.update(savings_id, savings)
