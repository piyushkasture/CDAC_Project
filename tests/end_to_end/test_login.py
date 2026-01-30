import pytest
from playwright.sync_api import expect
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from utils.base_test import BaseTest
from utils.DataReader import data

# Test class for login functionality validation
class TestLogin(BaseTest):

    @pytest.mark.parametrize("username,password,validity", data())
    def test_login(self, page, username, password, validity,logger):
        # Initialize page objects for login and dashboard pages
        login = LoginPage(page, logger)
        dashboard = DashboardPage(page)

        # Perform login with the provided credentials
        login.login(username, password)

        # Verify login results based on credential validity
        if validity=="valid":
            # Valid credentials should successfully log in and show dashboard
            logger.info("Successfully logged in")
            expect(dashboard.is_dashboard_visible()).to_be_visible()
        else:
            # Invalid credentials should show error or validation message
            try:
                # Check for invalid credentials error message
                logger.info("Getting error message, Invalid credentials")
                expect(login.get_error_message().first).to_be_visible()
            except AssertionError:
                # Check for required field validation message
                logger.info("Getting validation message, Required ")
                expect(login.get_required_field_message()).to_be_visible()