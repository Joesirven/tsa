import pytest
from unittest.mock import patch, Mock
from fastapi import Response
from routers.plans import create_plan
from queries.plans import PlansIn, PlansOut

@pytest.mark.asyncio
class TestCreatePlanEndpoint:

    @patch('routers.plans.PlansRepository')
    @patch('routers.plans.SavingsRepository')
    @patch('routers.plans.TransactionsRepository')
    @patch('routers.plans.authenticator.get_current_account_data')
    @patch('routers.plans.Response')
    async def test_create_plan_success(self, mock_response, mock_get_current_account_data, mock_transactions_repository, mock_savings_repository, mock_plans_repository):
        mock_plans_repo_instance = mock_plans_repository.return_value
        mock_savings_repo_instance = mock_savings_repository.return_value
        mock_transactions_repo_instance = mock_transactions_repository.return_value
        mock_get_current_account_data.return_value = {"user_id": 1}
        mock_response_instance = mock_response.return_value
        mock_response_instance.status_code = 200

        plan_input = PlansIn(
            start_of_budget="2023-09-01",
            end_of_budget="2023-12-31",
            trip_start_date="2023-09-15",
            trip_end_date="2023-12-31",
            destination="Vacation",
            monthly_budget=1000.00,
            users_id=1
        )

        expected_plan_output = PlansOut(id=1, **plan_input.dict())
        mock_plans_repo_instance.create.return_value = expected_plan_output

        created_plan = await create_plan(plan_input, mock_response_instance, mock_plans_repo_instance, mock_savings_repo_instance, mock_transactions_repo_instance)

        assert created_plan == expected_plan_output
        mock_plans_repo_instance.create.assert_called_once_with(plan_input)
        mock_response_instance.status_code = 200

    @patch('routers.plans.PlansRepository')
    @patch('routers.plans.SavingsRepository')
    @patch('routers.plans.TransactionsRepository')
    @patch('routers.plans.authenticator.get_current_account_data')
    @patch('routers.plans.Response')
    async def test_create_plan_failure(self, mock_response, mock_get_current_account_data, mock_transactions_repository, mock_savings_repository, mock_plans_repository):
        mock_plans_repo_instance = mock_plans_repository.return_value
        mock_savings_repo_instance = mock_savings_repository.return_value
        mock_transactions_repo_instance = mock_transactions_repository.return_value
        mock_get_current_account_data.return_value = {"user_id": 1}
        mock_response_instance = mock_response.return_value
        mock_response_instance.status_code = 500

        plan_input = PlansIn(
            start_of_budget="2023-09-01",
            end_of_budget="2023-12-31",
            trip_start_date="2023-09-15",
            trip_end_date="2023-12-31",
            destination="Vacation",
            monthly_budget=1000.00,
            users_id=1
        )

        expected_plan_output = PlansOut(id=1, **plan_input.dict())
        mock_plans_repo_instance.create.return_value = expected_plan_output

        created_plan = await create_plan(plan_input, mock_response_instance, mock_plans_repo_instance, mock_savings_repo_instance, mock_transactions_repo_instance)

        assert created_plan == expected_plan_output
        mock_plans_repo_instance.create.assert_called_once_with(plan_input)
        mock_response_instance.status_code = 500
