from fastapi import APIRouter, Depends, Response
from typing import Union, List, Optional
from queries.journals import Error, JournalIn, JournalOut, JournalRepository


router = APIRouter()


@router.post("/journal/create", response_model=Union[JournalOut, Error])
def create_journal(
  journal: JournalIn,
  repo: JournalRepository = Depends()
):
  return repo.create(journal)


@router.get("/journals", response_model=List[JournalOut])
def get_all(
  repo: JournalRepository = Depends(),
):
  return repo.get_all()

@router.put("/journal/{journal_id}", response_model=Union[Error, JournalOut])
def update_journal(
  journal_id: int,
  journal: JournalIn,
  repo: JournalRepository = Depends(),
) -> Union[Error, JournalOut]:
  return repo.update(journal_id, journal)

@router.delete("/journal/{journal_id}", response_model=bool)
def delete_journal(
  journal_id: int,
  repo: JournalRepository = Depends(),
) -> bool:
  return repo.delete(journal_id)

@router.get("/journal/{journal_id}", response_model=Optional[JournalOut])
def get_one_journal(
  journal_id: int,
  response: Response,
  repo: JournalRepository = Depends(),
) -> JournalOut:
  journal =repo.get_one(journal_id)
  if journal is None:
    response.status_code =404
  return journal
