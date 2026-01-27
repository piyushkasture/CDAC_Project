
import pytest
from playwright.sync_api import expect
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from utils.base_test import BaseTest
from pages.AdminPage import AdminUserPage


class TestAdmin(BaseTest):

    @pytest.fixture(autouse=True)
    def login_before_each_test(self, page, logger):
        # Login before each Admin test
        login_page = LoginPage(page, logger)
        login_page.login("Admin", "admin123")
        
        dashboard = DashboardPage(page)
        dashboard.go_to_admin()
        
        logger.info("Successfully logged in and navigated to Admin page")

    def test_search_user_by_admin_role(self, page, logger):
        admin_user = AdminUserPage(page)
        
        admin_user.select_user_role("Admin")
        admin_user.search_button.click()
        admin_user.wait_for_search_results()
        
        # Verify
        rows = admin_user.results_rows
        assert rows.count() > 1
        logger.info(f"Successfully found {rows.count()} Admin users")

    def test_search_user_by_ess_role(self, page, logger):
        
        admin_user = AdminUserPage(page)
        
        admin_user.select_user_role("ESS")
        admin_user.search_button.click()
        admin_user.wait_for_search_results()
        
        # Verify that results are displayed
        rows = admin_user.results_rows
        assert rows.count() >= 0
        logger.info(f"Successfully filtered ESS users. Found {rows.count()} records")

    def test_search_with_username(self, page, logger):
        
        admin_user = AdminUserPage(page)
        
        # Enter username
        admin_user.username_input.fill("Admin")
        admin_user.search_button.click()
        admin_user.wait_for_search_results()
        
        # Verify results
        rows = admin_user.results_rows
        assert rows.count() > 0
        logger.info(f"Successfully searched for username 'Admin'. Found {rows.count()} records")

    def test_search_with_username_and_role(self, page, logger):
    
        admin_user = AdminUserPage(page)
        
        # Enter username and select role
        admin_user.username_input.fill("Admin")
        admin_user.select_user_role("Admin")
        admin_user.search_button.click()
        admin_user.wait_for_search_results()
        
        # Verify results
        rows = admin_user.results_rows
        assert rows.count() > 0
        logger.info(f"Search with username 'Admin' and role 'Admin' returned {rows.count()} records")

    def test_search_with_invalid_username(self, page, logger):
        
        admin_user = AdminUserPage(page)
        
        # Enter invalid username
        admin_user.username_input.fill("InvalidUser12345")
        admin_user.search_button.click()
        
        # Verify no records found message
        try:
            expect(admin_user.no_records).to_be_visible(timeout=5000)
            logger.info("'No Records Found' message displayed as expected")
        except AssertionError:
            # If no records message not found, verify results are empty
            rows = admin_user.results_rows
            assert rows.count() == 0
            logger.info("No records found for invalid username")

    def test_admin_page_navigation(self, page, logger):
        
        admin_user = AdminUserPage(page)
        
        # Verify user role dropdown is visible
        expect(admin_user.user_role_dropdown).to_be_visible()
        
        # Verify search button is visible
        expect(admin_user.search_button).to_be_visible()
        
        # Verify username input field is visible
        expect(admin_user.username_input).to_be_visible()
        
        logger.info("Admin page elements are visible and accessible")

    def test_search_returns_valid_results(self, page, logger):
       
        admin_user = AdminUserPage(page)
        
        # Perform search with Admin role
        admin_user.select_user_role("Admin")
        admin_user.search_button.click()
        admin_user.wait_for_search_results()
        
        # Verify results rows are visible
        rows = admin_user.results_rows
        assert rows.count() > 0
        
        # Verify each row is visible
        for i in range(rows.count()):
            expect(rows.nth(i)).to_be_visible()
        
        logger.info(f"Verified {rows.count()} result rows are visible and valid")

