from fastapi import APIRouter, Depends, Response
from typing import Union, List, Optional
from queries.savings import SavingsIn, SavingsRepository, SavingsOut, Error
from authenticator import authenticator


router = APIRouter()


@router.post("/savings/create", response_model=Union[SavingsOut, Error])
async def create_savings(
  savings: SavingsIn,
  response: Response,
  repo: SavingsRepository = Depends(),
  user_data: dict = Depends(authenticator.get_current_account_data),
):
    return repo.create(savings)


@router.get("/savings", response_model=Union[List[SavingsOut], Error])
async def get_all(
  repo: SavingsRepository = Depends(),
  user_data: dict = Depends(authenticator.get_current_account_data),
):
  return repo.get_all()


@router.put("/savings/{savings_id}", response_model=Union[SavingsOut, Error])
async def update_savings(
  savings_id: int,
  savings: SavingsIn,
  repo: SavingsRepository = Depends(),
  user_data: dict = Depends(authenticator.get_current_account_data),
) -> Union[Error, SavingsOut]:
  return repo.update(savings_id, savings)


@router.delete("/savings/{savings_id}", response_model=bool)
async def delete_savings(
  savings_id: int,
  repo: SavingsRepository = Depends(),
  user_data: dict = Depends(authenticator.get_current_account_data),
) -> bool:
  return repo.delete(savings_id)



@router.get("/savings/{savings_id}", response_model=Optional[SavingsOut])
async def get_one_savings(
  savings_id: int,
  response: Response,
  repo: SavingsRepository = Depends(),
  user_data: dict = Depends(authenticator.get_current_account_data),
) -> SavingsOut:
  savings = repo.get_one(savings_id)
  if savings is None:
    response.status_code = 404
  return savings
