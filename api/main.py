from fastapi import FastAPI
from authenticator import authenticator
from fastapi.middleware.cors import CORSMiddleware
import os

from routers import (
    users,
    expenses,
    expenses_type_vo,
    journals,
    plans,
    savings,
    transactions
)

app = FastAPI()
app.include_router(authenticator.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/launch-details")
def launch_details():
    return {
        "launch_details": {
            "module": 3,
            "week": 17,
            "day": 5,
            "hour": 19,
            "min": "00"
        }
    }


app.include_router(users.router)
app.include_router(plans.router)
app.include_router(savings.router)
app.include_router(transactions.router)
app.include_router(journals.router)
app.include_router(expenses.router)
app.include_router(expenses_type_vo.router)
