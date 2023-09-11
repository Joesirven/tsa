import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from unittest.mock import patch, AsyncMock
from main import app
from queries.journals import JournalIn, JournalOut
from routers.journals import create_journal
from unittest.mock import AsyncMock

# Define your sample_journal here if not already defined
sample_journal = {
    "location": "Sample Location",
    "picture_url": "http://sample.url/image.jpg",
    "description": "This is a sample journal content.",
    "rating": 5,
    "date": "2023-01-01",
    "users_id": 1
}

# This is an example of the test adaptation for the 'test_create_journal_success' test:
@pytest.mark.anyio
@patch('routers.journals.JournalRepository', new_callable=AsyncMock)
@patch('routers.journals.authenticator.get_current_account_data')
async def test_create_journal_success(mock_get_current_account_data, mock_journal_repository):

    # Mocking the authenticator
    mock_get_current_account_data.return_value = {"user_id": 1}

    # Mocking the repo
    mock_journal = JournalOut(**sample_journal, id=1)  # Assuming this is the expected structure
    mock_journal_repository.return_value.create.return_value = mock_journal

    # Making the actual request
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/journal/create", json=sample_journal)

    assert response.status_code == 200
    assert response.json() == mock_journal.dict()
