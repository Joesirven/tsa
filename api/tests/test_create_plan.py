import pytest
import asyncio
from unittest.mock import patch, Mock
from fastapi import Response
from queries.plans import PlansRepository, PlansIn, PlansOut
from routers.plans import create_plan

@pytest.mark.asyncio
class TestCreatePlanEndpoint:

    @patch('routers.plans.PlansRepository')
    @patch('routers.plans.authenticator.get_current_account_data')
    @patch('routers.plans.Response')
    async def test_create_plan_success(self, mock_response, mock_get_current_account_data, mock_plans_repository):
        mock_repo_instance = mock_plans_repository.return_value
        mock_get_current_account_data.return_value = {"user_id": 1}
        mock_response_instance = mock_response.return_value
        mock_response_instance.status_code = 200

        plan_input = PlansIn(
            start_of_budget="2023-01-01",
            end_of_budget="2023-01-31",
            trip_start_date="2023-02-01",
            trip_end_date="2023-02-28",
            destination="Test Destination",
            monthly_budget=1000.00,
            users_id=1
        )

        expected_plan_output = PlansOut(id=1, **plan_input.dict())
        mock_repo_instance.create.return_value = expected_plan_output

        created_plan = await create_plan(plan_input, mock_response_instance, mock_repo_instance)

        assert created_plan == expected_plan_output
        mock_repo_instance.create.assert_called_once_with(plan_input)
        mock_response_instance.status_code = 200

    @patch('routers.plans.PlansRepository')
    @patch('routers.plans.authenticator.get_current_account_data')
    @patch('routers.plans.Response')
    async def test_create_plan_failure(self, mock_response, mock_get_current_account_data, mock_plans_repository):
        mock_repo_instance = mock_plans_repository.return_value
        mock_get_current_account_data.return_value = {"user_id": 1}
        mock_response_instance = mock_response.return_value
        mock_response_instance.status_code = 500

        plan_input = PlansIn(
            start_of_budget="2023-01-01",
            end_of_budget="2023-01-31",
            trip_start_date="2023-02-01",
            trip_end_date="2023-02-28",
            destination="Test Destination",
            monthly_budget=1000.00,
            users_id=1
        )

        expected_error = {"message": "Could not create plan."}
        mock_repo_instance.create.return_value = expected_error

        created_plan = await create_plan(plan_input, mock_response_instance, mock_repo_instance)

        assert created_plan == expected_error
        mock_repo_instance.create.assert_called_once_with(plan_input)
        mock_response_instance.status_code = 500