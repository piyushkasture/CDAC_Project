from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from utils.base_test import BaseTest
from pages.AdminPage import AdminPage


class TestAdmin(BaseTest):

    def test_navigate_to_admin_page(self):
        login_page = LoginPage(self.page)
        dashboard_page = DashboardPage(self.page)
        admin_page = AdminPage(self.page)

        login_page.login("Admin", "admin123")
        dashboard_page.go_to_admin()

        assert admin_page.is_admin_page_loaded()
