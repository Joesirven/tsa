from fastapi import (
  APIRouter,
  Depends,
  Response,
  HTTPException,
  status,
  Request,
  )
from typing import Union, List, Optional
from queries.users import Error, UserIn, UserOut, UserRepository, DuplicateUserError
from jwtdown_fastapi.authentication import Token
from authenticator import authenticator
from pydantic import BaseModel

class UserFrom(BaseModel):
  username: str
  password: str

class UserToken(Token):
  user: UserOut

class HttpError(BaseModel):
  detail: str


router = APIRouter()


@router.post("/user/sign-up", response_model=UserToken | HttpError)
async def create_user(
  user: UserIn,
  request: Request,
  response: Response,
  repo: UserRepository = Depends()
):
  hashed_password = authenticator.hashed_password(user.hashed_password)
  try:
    user = repo.create(user, hashed_password)
  except DuplicateUserError:
    raise HTTPExecption(
      status_code = status.HTTP_400_BAD_REQUEST,
      detail = " cannot create a new user with these credentials"
    )
  form = UserFrom(username=user.email, password=user.hashed_password)
  token = await authenticator.login(response, request, form, repo)
  return UserToken(user=user, **token.dict())


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
