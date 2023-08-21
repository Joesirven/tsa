from pydantic import BaseModel
from queries.pool import pool


class Error(BaseModel):
  message: str


class UserIn(BaseModel):
  first_name: str
  last_name: str
  email: str
  password: str
  password_confirmation: str


class UserOut(BaseModel):
  id: int
  first_name: str
  last_name: str
  email: str
  password: str
  password_confirmation: str


class UserRepository:
  def create(self, user: UserIn) -> UserOut:
    with pool.connection() as conn:
      with conn.cursor() as db:
        result = db.execute(
          """
          INSERT INTO users
            (
            first_name,
            last_name,
            email,
            password,
            password_confirmation
            )
          VALUES
            (%s, %s, %s, %s, %s)
          RETURNING id;
          """,
          [
          user.first_name,
          user.last_name,
          user.email,
          user.password,
          user.password_confirmation
          ]
        )
        id = result.fetchone()[0]
        old_data = user.dict()
        # return {"message": "Error, Could not create"}
        return UserOut(id=id, **old_data)
