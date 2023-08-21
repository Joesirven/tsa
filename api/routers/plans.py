from fastapi import APIRouter, Depends, Response
from queries.plans import (
  PlansIn,
  PlansOut,
  PlansRepository,
  Error,
)
from typing import Union, List, Optional


router = APIRouter()


@router.post("/plans/create", response_model=Union[PlansOut, Error])
def create_plan(
  plan: PlansIn,
  response: Response,
  repo: PlansRepository = Depends()
):
  return repo.create(plan)


@router.get("/plans", response_model=Union[Error, List[PlansOut]])
def get_all(
  repo: PlansRepository = Depends(),
):

  return repo.get_all()

@router.put("/plans/{plans_id}", response_model=Union[PlansOut, Error])
def update_plan(
  plan_id: int,
  plan: PlansIn,
  repo: PlansRepository = Depends(),
) -> Union[Error, PlansOut]:

  return repo.update(plan_id, plan)


@router.delete("/plans/{plans_id}", response_model=bool)
def delete_plan(
  plan_id: int,
  repo: PlansRepository = Depends(),
) -> bool:
  return repo.delete(plan_id)


@router.get("/plans/{plans_id}", response_model=Optional[PlansOut])
def get_one_plan(
  plan_id: int,
  response: Response,
  repo: PlansRepository = Depends(),
) -> PlansOut:
  plan = repo.get_one(plan_id)
  if plan is None:
    response.status_code = 404
  return plan
