from fastapi import APIRouter, Depends, Response
from typing import Union, List, Optional
from queries.journals import Error, JournalIn, JournalOut, JournalRepository
from authenticator import authenticator


router = APIRouter()


@router.post("/journal/create", response_model=Union[JournalOut, Error])
async def create_journal(
    journal: JournalIn,
    repo: JournalRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
):
    return repo.create(journal)


@router.get("/journals", response_model=List[JournalOut])
async def get_all(
    repo: JournalRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
):
    return repo.get_all()


@router.put("/journal/{journal_id}", response_model=Union[Error, JournalOut])
async def update_journal(
    journal_id: int,
    journal: JournalIn,
    repo: JournalRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
) -> Union[Error, JournalOut]:
    return repo.update(journal_id, journal)


@router.delete("/journal/{journal_id}", response_model=bool)
async def delete_journal(
    journal_id: int,
    repo: JournalRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
) -> bool:
    return repo.delete(journal_id)


@router.get("/journal/{journal_id}", response_model=Optional[JournalOut])
async def get_one_journal(
    journal_id: int,
    response: Response,
    repo: JournalRepository = Depends(),
    user_data: dict = Depends(authenticator.get_current_account_data),
) -> JournalOut:
    journal = repo.get_one(journal_id)
    if journal is None:
        response.status_code = 404
    return journal
