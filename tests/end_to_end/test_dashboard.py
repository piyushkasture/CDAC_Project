import pytest
from playwright.sync_api import expect

from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from utils.base_test import BaseTest
from utils.DataReader import data



# @pytest.mark.order(1)
class TestDashboard(BaseTest):

    # Verify Dashboard page loads after successful login
    def test_dashboard_load_after_login(self, dashboard_page):
        dashboard = DashboardPage(dashboard_page)
        expect(dashboard.is_dashboard_visible()).to_be_visible()

    # Verify Dashboard URL after login
    def test_dashboard_url(self, dashboard_page):
        assert "dashboard" in dashboard_page.url.lower()

    # # Navigate to Admin page for next test suite
    # def test_zzz_navigate_to_admin(self, dashboard_page):
    #     dashboard = DashboardPage(dashboard_page)
    #     dashboard.go_to_admin()
    #     # Wait for admin page to load
    #     dashboard_page.wait_for_load_state("networkidle")
    #     assert "admin" in dashboard_page.url.lower()

    # # Verify Dashboard page title
    # def test_dashboard_title(self, dashboard_page):
    #     expect(dashboard_page).to_have_title("OrangeHRM")

    # # Verify Dashboard header is visible
    # def test_dashboard_header_visible(self, dashboard_page):
    #     dashboard = DashboardPage(dashboard_page)
    #     expect(dashboard.is_dashboard_visible()).to_be_visible()

    # # Verify profile icon visibility on Dashboard
    # def test_profile_icon_visible(self, dashboard_page):
    #     dashboard = DashboardPage(dashboard_page)
    #     expect(dashboard.get_profile_icon()).to_be_visible()

    # # Verify Dashboard widgets section is displayed
    # def test_widgets_section_visible(self, dashboard_page):
    #     dashboard = DashboardPage(dashboard_page)
    #     expect(dashboard.get_widgets().first).to_be_visible()

    # # Verify at least one widget is displayed
    # def test_at_least_one_widget_present(self, dashboard_page):
    #     dashboard = DashboardPage(dashboard_page)
    #     assert dashboard.get_widgets().count() > 0

    # # Verify Dashboard page behavior on refresh
    # def test_dashboard_behavior_on_refresh(self, dashboard_page):
    #     dashboard = DashboardPage(dashboard_page)
    #     dashboard_page.reload()
    #     expect(dashboard.is_dashboard_visible()).to_be_visible()

    # # Verify Dashboard does not show error message on refresh
    # def test_no_error_message_on_refresh(self, dashboard_page):
    #     dashboard = DashboardPage(dashboard_page)
    #     dashboard_page.reload()
    #     expect(dashboard.get_error_message()).not_to_be_visible()

    # # Verify Dashboard page loads within acceptable time
    # def test_dashboard_load_time(self, dashboard_page):
    #     start_time = dashboard_page.evaluate("Date.now()")
    #     dashboard_page.reload()
    #     end_time = dashboard_page.evaluate("Date.now()")
    #     assert (end_time - start_time) < 5000

    # # Verify Dashboard elements are visible after refresh
    # def test_elements_visible_after_refresh(self, dashboard_page):
    #     dashboard = DashboardPage(dashboard_page)
    #     dashboard_page.reload()
    #     expect(dashboard.get_profile_icon()).to_be_visible()

    # # Verify no error or warning message on Dashboard
    # def test_no_warning_or_error_message(self, dashboard_page):
    #     dashboard = DashboardPage(dashboard_page)
    #     expect(dashboard.get_error_message()).not_to_be_visible()

    # # Verify Dashboard page scroll functionality
    # def test_dashboard_scroll(self, dashboard_page):
    #     dashboard_page.mouse.wheel(0, 2000)
    #     assert True

    # # Verify Dashboard widgets are clickable
    # def test_widgets_clickable(self, dashboard_page):
    #     dashboard = DashboardPage(dashboard_page)
    #     dashboard.get_widgets().first.click()
    #     assert True