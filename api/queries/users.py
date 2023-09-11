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
    def get_one(self, email: str) -> UserOutWithPassword:
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
            WHERE email=%s
            """,
                        [email],
                    )
                    entry = db.fetchone()
                    if entry is None:
                        return None
                    fields = [
                        "id",
                        "first_name",
                        "last_name",
                        "email",
                        "hashed_password",
                    ]
                    obj = {}
                    for i, col in enumerate(entry):
                        obj[fields[i]] = entry[i]
                    return self.user_in_to_out_password(obj)
        except Exception as e:
            return {"message": "could not get user "}

    def delete(self, user_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                    DELETE FROM users
                    WHERE id=%s
                  """,
                        [user_id],
                    )
                    return True
        except Exception as e:
            return False

    def update(self, user_id: int, user: UserIn) -> Union[UserOut, Error]:
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
                        ],
                    )

                    return self.user_in_to_out(user_id, user)
        except Exception as e:
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
                            hashed_password=entry[4],
                        )
                        for entry in db
                    ]
        except Exception as e:
            return {"message": "could not get users"}

    def create(
        self, user: UserIn, hashed_password: str
    ) -> UserOutWithPassword:
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
            RETURNING id;
            """,
                        [
                            user.first_name,
                            user.last_name,
                            user.email,
                            hashed_password,
                        ],
                    )
                    data = db.fetchone()[0]
                    user_dict = {
                        "id": data,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "email": user.email,
                    }
                    return UserOut(**user_dict)

        except Exception:
            raise DuplicateUserError()

    def user_in_to_out(self, id: int, user: UserIn):
        old_data = user.dict()
        return UserOut(id=id, **old_data)

    def user_in_to_out_password(self, user: UserIn):
        return UserOutWithPassword(**user)

    def record_to_user_out(self, entry):
        return UserOut(
            id=entry[0],
            first_name=entry[1],
            last_name=entry[2],
            email=entry[3],
            hashed_password=entry[4],
        )
