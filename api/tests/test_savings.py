from pydantic import BaseModel
from datetime import date
from authenticator import authenticator
from fastapi import FastAPI, APIRouter, Depends
from routers.savings import create_savings
from fastapi.testclient import TestClient
from typing import List
from decimal import Decimal


app = FastAPI()
router = APIRouter()
client = TestClient(app)


class SavingsOut(BaseModel):
    id: int
    current_amount_saved: Decimal
    final_goal_amount: Decimal
    plans_id: int


@router.get("/savings", response_model=List[SavingsOut])
async def get_all():
    savings = [
        SavingsOut(
            id=1,
            current_amount_saved=0,
            final_goal_amount=200,
            plans_id=1
        )
    ]
    return savings
app.include_router(router)


def test_get_savings():
    response = client.get("/savings")
    assert response.status_code == 200
    expected_response = [
        {
            "id":1,
            "current_amount_saved":0,
            "final_goal_amount":200,
            "plans_id":1
        }
    ]
    assert response.json() == expected_response
