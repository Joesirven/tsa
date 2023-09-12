import pytest
import asyncio
from unittest.mock import patch, Mock
from fastapi import Response
from queries.journals import JournalIn, JournalOut
from routers.journals import create_journal
from unittest.mock import AsyncMock


@pytest.mark.asyncio
class TestCreateJournalEndpoint:
    @patch("routers.journals.JournalRepository")
    @patch("routers.journals.authenticator.get_current_account_data")
    @patch("routers.journals.Response")
    async def test_create_journal_success(
        self,
        mock_response,
        mock_get_current_account_data,
        mock_journal_repository,
    ):
        mock_repo_instance = mock_journal_repository.return_value
        mock_get_current_account_data.return_value = {"user_id": 1}
        mock_response_instance = mock_response.return_value

        journal_input = JournalIn(
            location="Sample Location",
            picture_url="http://sample.url/image.jpg",
            description="This is a sample journal content.",
            rating=5,
            date="2023-01-01",
            users_id=1,
        )

        expected_journal_output = JournalOut(id=1, **journal_input.dict())
        mock_repo_instance.create.return_value = expected_journal_output
        mock_response_instance.create.return_value = expected_journal_output

        created_journal = await create_journal(
            journal_input, mock_response_instance, mock_repo_instance
        )

        assert created_journal == expected_journal_output

    @patch("routers.journals.JournalRepository")
    @patch("routers.journals.authenticator.get_current_account_data")
    @patch("routers.journals.Response")
    async def test_create_journal_failure(
        self,
        mock_response,
        mock_get_current_account_data,
        mock_journal_repository,
    ):
        mock_repo_instance = mock_journal_repository.return_value
        mock_get_current_account_data.return_value = {"user_id": 1}
        mock_response_instance = mock_response.return_value

        journal_input = JournalIn(
            location="Sample Location",
            picture_url="http://sample.url/image.jpg",
            description="This is a sample journal content.",
            rating=5,
            date="2023-01-01",
            users_id=1,
        )

        expected_error = {"message": "Could not create a journal entry"}
        mock_repo_instance.create.return_value = expected_error
        mock_response_instance.create.return_value = expected_error

        created_journal = await create_journal(
            journal_input, mock_response_instance, mock_repo_instance
        )

        assert created_journal == expected_error
