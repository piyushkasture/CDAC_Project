from utils.base_test import BaseTest
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from pages.LeavePage import LeavePage


class TestLeave(BaseTest):

    def test_navigate_to_leave_page(self):
        login = LoginPage(self.page)
        dashboard = DashboardPage(self.page)
        leave = LeavePage(self.page)

        login.login("Admin", "admin123")
        dashboard.go_to_leave()

        assert leave.is_leave_page_loaded(), \
            "Leave page did not load successfully"

    def test_search_leave_records(self):
        login = LoginPage(self.page)
        dashboard = DashboardPage(self.page)
        leave = LeavePage(self.page)

        login.login("Admin", "admin123")
        dashboard.go_to_leave()
        leave.search_leave("2024-01-01", "2024-31-12")

        assert "No Records Found" in leave.no_record_found(), \
            "Leave search failed"
