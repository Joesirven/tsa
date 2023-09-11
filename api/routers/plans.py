from fastapi import APIRouter, Depends, Response
from queries.plans import (
  PlansIn,
  PlansOut,
  PlansRepository,
  Error,
)
from queries.savings import SavingsRepository, SavingsIn
from routers.savings import create_savings
from queries.transactions import TransactionsRepository, TransactionsIn
from routers.transactions import create_transactions
from typing import Union, List, Optional
from authenticator import authenticator
from datetime import date
from dateutil.relativedelta import relativedelta
import calendar
from decimal import Decimal


router = APIRouter()


@router.post("/plans/create", response_model=Union[PlansOut, Error])
async def create_plan(
  plan: PlansIn,
  response: Response,
  plan_repo: PlansRepository = Depends(),
  savings_repo: SavingsRepository = Depends(),
  transactions_repo: TransactionsRepository = Depends(),
  user_data: dict = Depends(authenticator.get_current_account_data),
):
  print("here")
  new_plan = plan_repo.create(plan)

  start_date = date(new_plan.start_of_budget.year, new_plan.start_of_budget.month, new_plan.start_of_budget.day)
  end_date = date(new_plan.end_of_budget.year, new_plan.end_of_budget.month, new_plan.end_of_budget.day)
  duration = relativedelta(end_date, start_date).months + 1
  final_goal_amount = new_plan.monthly_budget * Decimal(duration)

  savings = SavingsIn(
    current_amount_saved = Decimal(0.00),
    final_goal_amount = final_goal_amount,
    plans_id = new_plan.id
  )
  new_savings = savings_repo.create(savings)

  for i in range(duration):
    new_date = start_date + relativedelta(months=i)
    transaction = TransactionsIn(
      amount_saved = new_plan.monthly_budget,
      date = new_date,
      if_saved = False,
      savings_id = new_savings.id
    )
    new_transaction = transactions_repo.create(transaction)
    print(transaction)
  return new_plan


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
