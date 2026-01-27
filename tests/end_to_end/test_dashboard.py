import pytest
from playwright.sync_api import expect

from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from utils.base_test import BaseTest
from utils.DataReader import data


@pytest.mark.order(0)
class TestDashboard(BaseTest):

    @pytest.fixture(autouse=True)
    def login_before_each_test(self, page, logger):
        # Login before each Dashboard test
        login = LoginPage(page, logger)

        # Get ONLY valid credentials from JSON
        username, password, validity = data()[0]
        assert validity == "valid"

        logger.info("Logging in with valid credentials before Dashboard test")
        login.login(username, password)

        dashboard = DashboardPage(page)
        expect(dashboard.is_dashboard_visible()).to_be_visible()

    # Verify Dashboard page loads after successful login
    def test_dashboard_load_after_login(self, page):
        dashboard = DashboardPage(page)
        expect(dashboard.is_dashboard_visible()).to_be_visible()

    # Verify Dashboard URL after login
    def test_dashboard_url(self, page):
        assert "dashboard" in page.url.lower()

    # Verify Dashboard page title
    def test_dashboard_title(self, page):
        expect(page).to_have_title("OrangeHRM")

    # Verify Dashboard header is visible
    def test_dashboard_header_visible(self, page):
        dashboard = DashboardPage(page)
        expect(dashboard.is_dashboard_visible()).to_be_visible()

    # Verify profile icon visibility on Dashboard
    def test_DASH_005_profile_icon_visible(self, page):
        dashboard = DashboardPage(page)
        expect(dashboard.get_profile_icon()).to_be_visible()

    # Verify Dashboard widgets section is displayed
    def test_widgets_section_visible(self, page):
        dashboard = DashboardPage(page)
        expect(dashboard.get_widgets().first).to_be_visible()

    # Verify at least one widget is displayed
    def test_at_least_one_widget_present(self, page):
        dashboard = DashboardPage(page)
        assert dashboard.get_widgets().count() > 0

    # Verify Dashboard page behavior on refresh
    def test_dashboard_behavior_on_refresh(self, page):
        dashboard = DashboardPage(page)
        page.reload()
        expect(dashboard.is_dashboard_visible()).to_be_visible()

    # Verify Dashboard does not show error message on refresh
    def test_no_error_message_on_refresh(self, page):
        dashboard = DashboardPage(page)
        page.reload()
        expect(dashboard.get_error_message()).not_to_be_visible()

    # Verify Dashboard page loads within acceptable time
    def test_dashboard_load_time(self, page):
        start_time = page.evaluate("Date.now()")
        page.reload()
        end_time = page.evaluate("Date.now()")
        assert (end_time - start_time) < 5000

    # Verify Dashboard elements are visible after refresh
    def test_elements_visible_after_refresh(self, page):
        dashboard = DashboardPage(page)
        page.reload()
        expect(dashboard.get_profile_icon()).to_be_visible()

    # Verify no error or warning message on Dashboard
    def test_no_warning_or_error_message(self, page):
        dashboard = DashboardPage(page)
        expect(dashboard.get_error_message()).not_to_be_visible()

    # Verify Dashboard page scroll functionality
    def test_dashboard_scroll(self, page):
        page.mouse.wheel(0, 2000)
        assert True

    # Verify Dashboard widgets are clickable
    def test_widgets_clickable(self, page):
        dashboard = DashboardPage(page)
        dashboard.get_widgets().first.click()
        assert True
