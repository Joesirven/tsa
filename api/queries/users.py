from pydantic import BaseModel
from queries.pool import pool
from typing import List, Union, Optional
from fastapi import HTTPException, status


class DuplicateUserError(ValueError):
  pass


class Error(BaseModel):
  message: str


class UserIn(BaseModel):
  first_name: str
  last_name: str
  email: str
  password: str


class UserOut(BaseModel):
  id: int
  first_name: str
  last_name: str
  email: str


class UserOutWithPassword(UserOut):
  hashed_password: str


class UserRepository:
  def get_one(self, id: int) -> UserOutWithPassword:
    print(f"id in get {id} ")
    try:
      with pool.connection() as conn:
        with conn.cursor() as db:
          db.execute(
            """
              SELECT
                id,
                first_name,
                last_name,
                email,
                hashed_password
                FROM users
                WHERE id=%s
              """,
                [id]
          )
          print(f"db in get {db}")
          entry = db.fetchone()
          print(f"in get {entry}")
          if entry is None:
            return None
          return self.user_in_to_out_password(entry)
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
              hashed_password = %s
            WHERE id = %s
            """,
              [
                user.first_name,
                user.last_name,
                user.email,
                user.hashed_password,
                user_id,
              ]
          )

          return self.user_in_to_out(user_id, user)
    except Exception as e:
      print(e)
      return {"message": "could not update user "}


  def get_all(self) -> Union[Error, List[UserOutWithPassword]]:
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
            hashed_password
            FROM users
            ORDER BY id
          """
          )
          return [
            UserOutWithPassword(
              id=entry[0],
              first_name=entry[1],
              last_name=entry[2],
              email=entry[3],
              hashed_password=entry[4]
            )
            for entry in db
          ]
    except Exception as e:
      print(e)
      return {"message": "could not get users"}


  def create(self, user: UserIn, hashed_password: str) -> UserOutWithPassword:
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
              hashed_password
              )
            VALUES
              (%s, %s, %s, %s)
            RETURNING id, first_name, last_name, email, hashed_password;
            """,
            [
            user.first_name,
            user.last_name,
            user.email,
            hashed_password
            ]
          )
          data = db.fetchone()
          print(f"data from sql {data}")
          fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "hashed_password"
          ]
          obj = {}
          for i, col in enumerate(data):
            obj[fields[i]] = data[i]
          print(f"this is obj {obj}")
          entry = self.get_one(obj["id"])
          print(f"This is entry: {entry}")
          # return self.user_in_to_out_password(id, user)

    except DuplicateUserError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create an account with those credentials",
        )

  def user_in_to_out(self, id:int, user: UserIn):
    old_data = user.dict()
    return UserOut(id=id, **old_data)


  def user_in_to_out_password(self, id:int, user: UserIn):
    old_data = user.dict()
    print(f"this is is old data: {old_data}")
    return UserOutWithPassword(id=id, **old_data)



  def record_to_user_out(self, entry):
        return UserOut(
          id=entry[0],
          first_name=entry[1],
          last_name=entry[2],
          email=entry[3],
          hashed_password=entry[4]
        )
