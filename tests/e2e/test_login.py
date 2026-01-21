import pytest
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from utils.base_test import BaseTest


# class TestLogin(BaseTest):
#     def test_login(self):
#         self.page.fill("Admin", "admin123")

class TestLogin(BaseTest):

    def test_valid_login(self):
        login_page = LoginPage(self.page)
        dashboard_page = DashboardPage(self.page)

        login_page.login("Admin", "admin123")

        assert dashboard_page.is_dashboard_visible(), \
            "Dashboard is not visible after valid login"

    def test_invalid_login(self):
        login_page = LoginPage(self.page)

        login_page.login("Admin", "wrongpassword")

        assert "Invalid credentials" in login_page.get_error_message(), \
            "Error message not displayed for invalid login"
