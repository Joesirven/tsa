from fastapi.testclient import TestClient
from main import app
from queries.users import UserRepository

client = TestClient(app)

class MockUserRepository:
  def get_all(self):
    return []

def test_get_all_users():
  app.dependency_overrides[UserRepository] = MockUserRepository
  response = client.get("/users")
  assert response.status_code == 200
  app.dependency_overrides = {}
