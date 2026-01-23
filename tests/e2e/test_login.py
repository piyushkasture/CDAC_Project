import pytest
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from utils.base_test import BaseTest
from utils.DataReader import test_data

class TestLogin(BaseTest):
    @pytest.mark.parametrize("username,password", test_data())

    def test_login(self, page, username, password):
        login = LoginPage(page)
        dashboard = DashboardPage(page)

        login.login(username, password)

        if username == "Admin" and password == "admin123":
            assert dashboard.is_dashboard_visible(), \
                f"Login failed for valid data: {username}/{password}"
        else:
            assert ("Required" in login.get_required_field_message() or "Invalid" in login.get_error_message())
            # assert (login.get_required_field_message() or login.get_error_message())