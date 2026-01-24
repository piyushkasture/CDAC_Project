import pytest
from playwright.sync_api import expect

from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from utils.base_test import BaseTest
from utils.DataReader import data

class TestLogin(BaseTest):
    @pytest.mark.parametrize("username,password,validity", data())

    def test_login(self, page, username, password, validity,logger):
        login = LoginPage(page, logger)
        dashboard = DashboardPage(page)

        login.login(username, password)

        if validity=="valid":
            logger.info("Successfully logged in")
            assert dashboard.is_dashboard_visible()
        else:
            try:
                logger.info("Getting error message, Invalid credentials")
                expect(login.get_error_message()).to_be_visible()
            except AssertionError:
                # If not invalid, then it must be required
                logger.info("Getting validation message, Required ")
                expect(login.get_required_field_message()).to_be_visible()

            # expect(login.get_error_message().to_be_visible() or login.get_required_field_message().to_be_visible(), f"Login failed for invalid data: {username}/{password}")
            # assert ("Required" in login.get_required_field_message() or "Invalid" in login.get_error_message())
            # assert (login.get_required_field_message() or login.get_error_message())