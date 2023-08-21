from fastapi import APIRouter, Depends, Response
from typing import Union, List
from queries.transactions import TransactionsIn, TransactionsRepository, TransactionsOut, Error


router = APIRouter()


@router.post("/transactions/create", response_model=Union[TransactionsOut, Error])
def create_transactions(
  transactions: TransactionsIn,
  response: Response,
  repo: TransactionsRepository = Depends()
):
    response.status_code = 400
    return repo.create(transactions)


@router.get("/transactions", response_model=Union[Error, List[TransactionsOut]])
def get_all(
  repo: TransactionsRepository = Depends(),
):
  return repo.get_all()
