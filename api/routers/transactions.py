from fastapi import APIRouter, Depends, Response
from typing import Union, List, Optional
from queries.transactions import TransactionsIn, TransactionsRepository, TransactionsOut, Error


router = APIRouter()


@router.post("/transactions/create", response_model=Union[TransactionsOut, Error])
def create_transactions(
  transactions: TransactionsIn,
  repo: TransactionsRepository = Depends()
):
    return repo.create(transactions)


@router.get("/transactions", response_model=Union[Error, List[TransactionsOut]])
def get_all(
  repo: TransactionsRepository = Depends(),
):
  return repo.get_all()


@router.put("/transactions/{transactions_id}", response_model=Union[TransactionsOut, Error])
def update_transactions(
  transactions_id: int,
  transactions: TransactionsIn,
  repo: TransactionsRepository = Depends(),
) -> Union[TransactionsOut, Error]:
  return repo.update(transactions_id, transactions)


@router.delete("/transactions/{transactions_id}", response_model=bool)
def delete_transactions(
  transactions_id: int,
  repo: TransactionsRepository = Depends(),
) -> bool:
  return repo.delete(transactions_id)


@router.get("/transactions/{transactions_id}", response_model=Optional[TransactionsOut])
def get_one_transaction(
  transactions_id: int,
  response: Response,
  repo: TransactionsRepository = Depends(),
) -> TransactionsOut:
  transactions = repo.get_one(transactions_id)
  if transactions is None:
    response.status_code = 404
  return transactions
