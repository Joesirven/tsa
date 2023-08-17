from fastapi import APIRouter, Depends, Response
from typing import Union
from queries.journals import Error, JournalIn, JournalOut, JournalRepository


router = APIRouter()


@router.post("/journal/create", response_model=Union[JournalOut, Error])
def create_journal(
  journal: JournalIn,
  response: Response,
  repo: JournalRepository = Depends()
):
  response.status_code = 400
  return repo.create(journal)
