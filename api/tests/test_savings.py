import pytest
import asyncio
from unittest.mock import patch, Mock
from fastapi import Response
from queries.savings import SavingsRepository, SavingsIn, SavingsOut
from routers.savings import create_savings

@pytest.mark.asyncio
class TestCreateSavingsEndpoint:

    @patch('routers.savings.SavingsRepository')
    @patch('routers.savings.authenticator.get_current_account_data')
    @patch('routers.savings.Response')
    async def test_create_savings_success(self, mock_response, mock_get_current_account_data, mock_savings_repository):
        mock_repo_instance = mock_savings_repository.return_value
        mock_get_current_account_data.return_value = {"user_id": 1}
        mock_response_instance = mock_response.return_value
        mock_response_instance.status_code = 200

        savings_input = SavingsIn(
            current_amount_saved=0.00,
            final_goal_amount=5000.00,
            plans_id=1
        )

        expected_savings_output = SavingsOut(id=1, **savings_input.dict())
        mock_repo_instance.create.return_value = expected_savings_output

        created_savings = await create_savings(savings_input, mock_response_instance, mock_repo_instance)

        assert created_savings == expected_savings_output
        mock_repo_instance.create.assert_called_once_with(savings_input)
        mock_response_instance.status_code = 200

    @patch('routers.savings.SavingsRepository')
    @patch('routers.savings.authenticator.get_current_account_data')
    @patch('routers.savings.Response')
    async def test_create_savings_failure(self, mock_response, mock_get_current_account_data, mock_savings_repository):
        mock_repo_instance = mock_savings_repository.return_value
        mock_get_current_account_data.return_value = {"user_id": 1}
        mock_response_instance = mock_response.return_value
        mock_response_instance.status_code = 500

        savings_input = SavingsIn(
            current_amount_saved=0.00,
            final_goal_amount=5000.00,
            plans_id=1
        )

        expected_error = {"message": "Could not create savings."}
        mock_repo_instance.create.return_value = expected_error

        created_savings = await create_savings(savings_input, mock_response_instance, mock_repo_instance)

        assert created_savings == expected_error
        mock_repo_instance.create.assert_called_once_with(savings_input)
        mock_response_instance.status_code = 500
