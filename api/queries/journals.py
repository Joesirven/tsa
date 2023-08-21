from pydantic import BaseModel
from queries.pool import pool
from datetime import date
from typing import List, Union


class Error(BaseModel):
    message: str


class JournalIn(BaseModel):
  location: str
  picture_url: str
  description: str
  rating: int
  date: date


class JournalOut(BaseModel):
  id: int
  location: str
  picture_url: str
  description: str
  rating: int
  date: date



class JournalRepository:
  def get_all(self) -> Union[Error, List[JournalOut]]:
    try:
      with pool.connection() as conn:
        with conn.cursor() as db:
          result = db.execute(
          """
          SELECT
            id,
            location,
            picture_url,
            description,
            rating,
            date
            FROM journals
            ORDER BY date
          """
          )
          return [
            JournalOut(
              id=entry[0],
              location=entry[1],
              picture_url=entry[2],
              description=entry[3],
              rating=entry[4],
              date=entry[5]
            )
            for entry in db
          ]
    except Exception as e:
      return {"message": e}


  def create(self, journal: JournalIn) -> JournalOut:
    try:
      with pool.connection() as conn:
        with conn.cursor() as db:
          result = db.execute(
            """
            INSERT INTO journals
              (
              location,
              picture_url,
              description,
              rating,
              date
              )
            VALUES
              (%s, %s, %s, %s, %s)
            RETURNING id;
            """,
            [
            journal.location,
            journal.picture_url,
            journal.description,
            journal.rating,
            journal.date,
            ]
          )
          id = result.fetchone()[0]
          old_data = journal.dict()
          return JournalOut(id=id, **old_data)
    except Exception as e:
      return {"message": e}
