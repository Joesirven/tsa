from fastapi.testclient import TestClient
from main import app
from queries.users import UserRepository, UserOutWithPassword
from pydantic import BaseModel

client = TestClient(app)

class MockUserOutWithPassword(BaseModel):
  id: int
  first_name: str
  last_name: str
  email: str
  hashed_password: str

class MockUserRepository(BaseModel):
  def get_all(self):
    return MockUserOutWithPassword(
      id =  1,
      first_name = "britlee",
      last_name = "britlee",
      email =  "britlee",
      hashed_password = "$2b$12$i4aMPNEXd84/0uPx8MtPQOw/xzE5zDtmSOAsEYSq2uNzeI2b8k79O"
    )

def test_get_all_users():
  app.dependency_overrides[UserRepository] = MockUserRepository
  response = client.get("/users")
  assert response.status_code == 200
  app.dependency_overrides = {}
  