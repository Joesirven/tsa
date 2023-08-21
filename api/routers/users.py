from fastapi import APIRouter, Depends, Response
from typing import Union, List, Optional
from queries.users import Error, UserIn, UserOut, UserRepository


router = APIRouter()


@router.post("/user/sign-up", response_model=Union[UserOut, Error])
def create_user(
  user: UserIn,
  repo: UserRepository = Depends()
):
  return repo.create(user)


@router.get("/users", response_model=List[UserOut])
def get_all(
  repo: UserRepository = Depends(),
):
  return repo.get_all()

@router.put("/user/{user_id}", response_model=Union[Error, UserOut])
def update_journal(
  user_id: int,
  user: UserIn,
  repo: UserRepository = Depends(),
) -> Union[Error, UserOut]:
  return repo.update(user_id, user)

@router.delete("/user/{user_id}", response_model=bool)
def delete_journal(
  user_id: int,
  repo: UserRepository = Depends(),
) -> bool:
  return repo.delete(user_id)

@router.get("/user/{user_id}", response_model=Optional[UserOut])
def get_one_journal(
  user_id: int,
  response: Response,
  repo: UserRepository = Depends(),
) -> UserOut:
  user =repo.get_one(user_id)
  if user is None:
    response.status_code =404
  return user
