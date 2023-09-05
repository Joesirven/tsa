from fastapi import APIRouter, Depends, Response
from typing import Union, List, Optional
from queries.trip_advisor import
from authenticator import authenticator


router = APIRouter()
