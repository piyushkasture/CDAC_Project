
from playwright.sync_api import expect
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from utils.base_test import BaseTest
from pages.AdminPage import AdminUserPage


class TestAdmin(BaseTest):

    def test_search_user_by_admin_role(self, page, logger):
        # Initialize page objects with logger
        login_page = LoginPage(page, logger)
        login_page.login("Admin", "admin123")

        dashboard = DashboardPage(page)
        dashboard.go_to_admin()

        # Initialize AdminUserPage without logger parameter
        admin_user = AdminUserPage(page)
        # admin_user.wait_for_users_page()
        admin_user.select_user_role("Admin")
        admin_user.search_button.click()
        admin_user.wait_for_search_results()
        # Verify
        rows = admin_user.results_rows
        assert rows.count() > 1

