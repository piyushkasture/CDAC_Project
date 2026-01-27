from utils.base_test import BaseTest
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from pages.RecruitmentPage import RecruitmentPage


class TestRecruitment(BaseTest):

    def test_navigate_to_recruitment_page(self):
        login = LoginPage(self.page)
        dashboard = DashboardPage(self.page)
        recruitment = RecruitmentPage(self.page)

        login.login("Admin", "admin123")
        dashboard.go_to_recruitment()

        assert recruitment.is_recruitment_page_loaded()

    def test_search_candidate(self):
        login = LoginPage(self.page)
        dashboard = DashboardPage(self.page)
        recruitment = RecruitmentPage(self.page)

        login.login("Admin", "admin123")
        dashboard.go_to_recruitment()
        recruitment.search_candidate("John  Doe")

        assert recruitment.record_found()
