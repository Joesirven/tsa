from fastapi import APIRouter, Depends
from queries.plans import PlansIn, PlansRepository


router = APIRouter()


@router.post("/plans")
def create_plan(
  plan: PlansIn,
  repo: PlansRepository = Depends()
):
  return repo.create(plan)
