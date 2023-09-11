from fastapi import APIRouter, Depends, Response
from typing import Union, List, Optional
from queries.transactions import (
    TransactionsIn,
    TransactionsRepository,
    TransactionsOut,
    Error,
)
from queries.savings import SavingsIn, SavingsRepository
from routers.savings import update_savings, get_one_savings
from authenticator import authenticator


router = APIRouter()


@router.post(
    "/transactions/create", response_model=Union[TransactionsOut, Error]
)
async def create_transactions(
    transactions: TransactionsIn,
    repo: TransactionsRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
):
    return repo.create(transactions)


@router.get(
    "/transactions", response_model=Union[Error, List[TransactionsOut]]
)
async def get_all(
    transactions_repo: TransactionsRepository = Depends(),
    savings_repo: SavingsRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
):
    all_transactions = transactions_repo.get_all()
    savings_repo.calculate_current_amount_saved(transactions_repo)
    return all_transactions


@router.put(
    "/transactions/{transactions_id}",
    response_model=Union[TransactionsOut, Error],
)
async def update_transactions(
    transactions_id: int,
    transactions: TransactionsIn,
    transactions_repo: TransactionsRepository = Depends(),
    savings_repo: SavingsRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
) -> Union[TransactionsOut, Error]:
    updated_transaction = transactions_repo.update(
        transactions_id, transactions
    )
    savings_repo.calculate_current_amount_saved(transactions_repo)
    return updated_transaction


@router.delete("/transactions/{transactions_id}", response_model=bool)
async def delete_transactions(
    transactions_id: int,
    repo: TransactionsRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
) -> bool:
    return repo.delete(transactions_id)


@router.get(
    "/transactions/{transactions_id}", response_model=Optional[TransactionsOut]
)
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
