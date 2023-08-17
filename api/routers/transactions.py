from fastapi import APIRouter, Depends
from typing import Union
from queries.transactions import TransactionsIn, TransactionsRepository, TransactionsOut, Error


router = APIRouter()


@router.post("/transactions/create", response_model = Union[TransactionsOut, Error])
def create_transactions(
  transactions: TransactionsIn,
  repo: TransactionsRepository = Depends()
):
    return repo.create(transactions)