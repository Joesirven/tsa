from fastapi import APIRouter, Depends, Response
from queries.plans import (
  PlansIn,
  PlansOut,
  PlansRepository,
  Error,
)
from typing import Union, List, Optional
from authenticator import authenticator


router = APIRouter()


@router.post("/plans/create", response_model=Union[PlansOut, Error])
async def create_plan(
  plan: PlansIn,
  response: Response,
  repo: PlansRepository = Depends(),
  user_data: dict = Depends(authenticator.get_current_account_data),
):
  print("here")
  return repo.create(plan)


@router.get("/plans", response_model=Union[Error, List[PlansOut]])
async def get_all(
  repo: PlansRepository = Depends(),
  user_data: dict = Depends(authenticator.get_current_account_data),
):

  return repo.get_all()

@router.put("/plans/{plan_id}", response_model=Union[PlansOut, Error])
async def update_plan(
  plan_id: int,
  plan: PlansIn,
  repo: PlansRepository = Depends(),
  user_data: dict = Depends(authenticator.get_current_account_data),
) -> Union[Error, PlansOut]:

  return repo.update(plan_id, plan)


@router.delete("/plans/{plan_id}", response_model=bool)
async def delete_plan(
  plan_id: int,
  repo: PlansRepository = Depends(),
  user_data: dict = Depends(authenticator.get_current_account_data),
) -> bool:
  return repo.delete(plan_id)


@router.get("/plans/{plan_id}", response_model=Optional[PlansOut])
async def get_one_plan(
  plan_id: int,
  response: Response,
  repo: PlansRepository = Depends(),
  user_data: dict = Depends(authenticator.get_current_account_data),
) -> PlansOut:
  plan = repo.get_one(plan_id)
  if plan is None:
    response.status_code = 404
  return plan
