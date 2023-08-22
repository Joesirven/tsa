from pydantic import BaseModel
from queries.pool import pool
from typing import List, Union, Optional


class DuplicateUserError(ValueError):
  pass


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


class UserOutWithPassword(UserOut):
  hashed_password: str


class UserRepository:
  def get_one(self, user_id: int) -> Optional[UserOut]:
    try:
      with pool.connection() as conn:
        with conn.cursor() as db:
          result = db.execute(
            """
              SELECT
                id,
                first_name,
                last_name,
                email,
                password,
                password_confirmation
                FROM users
                WHERE id=%s
              """,
                [user_id]
          )
          entry = result.fetchone()
          if entry is None:
            return None
          return self.record_to_user_out(entry)
    except Exception as e:
      print(e)
      return {"message": "could not get user "}


  def delete(self, user_id:int)-> bool:
    try:
      with pool.connection() as conn:
              with conn.cursor() as db:
                db.execute(
                  """
                    DELETE FROM users
                    WHERE id=%s
                  """,
                  [user_id]
                )
                return True
    except Exception as e:
      print(e)
      return False


  def update(self, user_id:int, user: UserIn) -> Union[UserOut, Error]:
    try:
      with pool.connection() as conn:
        with conn.cursor() as db:
          db.execute(
            """
            UPDATE users

            SET
              first_name = %s,
              last_name = %s,
              email = %s,
              password = %s,
              password_confirmation = %s
            WHERE id = %s
            """,
              [
                user.first_name,
                user.last_name,
                user.email,
                user.password,
                user.password_confirmation,
                user_id,
              ]
          )

          return self.user_in_to_out(user_id, user)
    except Exception as e:
      print(e)
      return {"message": "could not update user "}


  def get_all(self) -> Union[Error, List[UserOut]]:
    try:
      with pool.connection() as conn:
        with conn.cursor() as db:
          result = db.execute(
          """
          SELECT
            id,
            first_name,
            last_name,
            email,
            password,
            password_confirmation
            FROM users
            ORDER BY id
          """
          )
          return [
            UserOut(
              id=entry[0],
              first_name=entry[1],
              last_name=entry[2],
              email=entry[3],
              password=entry[4],
              password_confirmation=entry[5]
            )
            for entry in db
          ]
    except Exception as e:
      print(e)
      return {"message": "could not get users"}


  def create(self, user: UserIn, hashed_password: str) -> UserOut:
    try:
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
          return self.user_in_to_out(id, user)
    except DuplicateUserError():
        raise DuplicateUserError()


  def user_in_to_out(self, id:int, user: UserIn):
    old_data = user.dict()
    return UserOut(id=id, **old_data)


  def record_to_user_out(self, entry):
        return UserOut(
          id=entry[0],
          first_name=entry[1],
          last_name=entry[2],
          email=entry[3],
          password=entry[4],
          password_confirmation=entry[5]
        )
