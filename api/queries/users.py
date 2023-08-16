from pydantic import BaseModel


class UserIn(BaseModel):
  first_name: str
  last_name: str
  email: str
  password: str
  password_confirmation: str
  
