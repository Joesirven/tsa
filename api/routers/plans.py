from fastapi import APIRouter, Depends, Response
from queries.plans import (
  PlansIn,
  PlansOut,
  PlansRepository,
  Error,
)
from typing import Union, List


router = APIRouter()


@router.post("/plans/create", response_model=Union[PlansOut, Error])
def create_plan(
  plan: PlansIn,
  response: Response,
  repo: PlansRepository = Depends()
):
  response.status_code = 400
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
