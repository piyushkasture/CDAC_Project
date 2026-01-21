from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from utils.base_test import BaseTest
from pages.PIMPage import PIMPage


class TestPIM(BaseTest):

    def test_navigate_to_pim_page(self):
        login_page = LoginPage(self.page)
        dashboard_page = DashboardPage(self.page)
        pim_page = PIMPage(self.page)

        login_page.login("Admin", "admin123")
        dashboard_page.go_to_pim()

        assert pim_page.is_pim_page_loaded(), \
            "PIM page did not load successfully"
