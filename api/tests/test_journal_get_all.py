from pydantic import BaseModel
from datetime import date
from authenticator import authenticator
from fastapi import FastAPI, APIRouter, Depends
from routers.journals import create_journal
from fastapi.testclient import TestClient
from typing import List


app = FastAPI()
router = APIRouter()
client = TestClient(app)


class JournalOut(BaseModel):
    id: int
    location: str
    picture_url: str
    description: str
    rating: int
    date: date
    users_id: int


@router.get("/journals", response_model=List[JournalOut])
async def get_all():
    journals = [
        JournalOut(
            location="Sample Location",
            picture_url="http://sample.url/image.jpg",
            description="This is a sample journal content.",
            rating=5,
            date="2023-01-01",
            users_id=1,
            id=1
        )
    ]
    return journals
app.include_router(router)


def test_get_journal():
    response = client.get("/journals")
    assert response.status_code == 200
    expected_response = [
        {
            "id": 1,
            "location": "Sample Location",
            "picture_url": "http://sample.url/image.jpg",
            "description": "This is a sample journal content.",
            "rating": 5,
            "date": "2023-01-01",
            "users_id": 1
        }
    ]
    assert response.json() == expected_response
