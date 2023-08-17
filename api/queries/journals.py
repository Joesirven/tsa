from pydantic import BaseModel
from queries.pool import pool
from datetime import date


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
  def create(self, journal: JournalIn) -> JournalOut:
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
        return {"message": "Error, Could not create journal"}
        return JournalOut(id=id, **old_data)