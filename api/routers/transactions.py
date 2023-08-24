from fastapi import APIRouter, Depends, Response
from typing import Union, List, Optional
from queries.transactions import TransactionsIn, TransactionsRepository, TransactionsOut, Error
from authenticator import authenticator


router = APIRouter()


@router.post("/transactions/create", response_model=Union[TransactionsOut, Error])
async def create_transactions(
  transactions: TransactionsIn,
  repo: TransactionsRepository = Depends(),
  user_data: dict = Depends(authenticator.get_current_account_data),
):
    return repo.create(transactions)


@router.get("/transactions", response_model=Union[Error, List[TransactionsOut]])
async def get_all(
  repo: TransactionsRepository = Depends(),
  user_data: dict = Depends(authenticator.get_current_account_data),
):
  return repo.get_all()


@router.put("/transactions/{transactions_id}", response_model=Union[TransactionsOut, Error])
async def update_transactions(
  transactions_id: int,
  transactions: TransactionsIn,
  repo: TransactionsRepository = Depends(),
  user_data: dict = Depends(authenticator.get_current_account_data),
) -> Union[TransactionsOut, Error]:
  return repo.update(transactions_id, transactions)


@router.delete("/transactions/{transactions_id}", response_model=bool)
async def delete_transactions(
  transactions_id: int,
  repo: TransactionsRepository = Depends(),
  user_data: dict = Depends(authenticator.get_current_account_data),
) -> bool:
  return repo.delete(transactions_id)


@router.get("/transactions/{transactions_id}", response_model=Optional[TransactionsOut])
async def get_one_transaction(
  transactions_id: int,
  response: Response,
  repo: TransactionsRepository = Depends(),
  user_data: dict = Depends(authenticator.get_current_account_data),
) -> TransactionsOut:
  transactions = repo.get_one(transactions_id)
  if transactions is None:
    response.status_code = 404
  return transactions
