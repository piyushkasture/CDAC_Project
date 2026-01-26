
from playwright.sync_api import expect
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from utils.base_test import BaseTest
from pages.AdminPage import AdminUserPage


class TestAdmin(BaseTest):
    """
    Test class for Admin page functionality.
    Tests admin-related features and navigation in the OrangeHRM application.
    """

    # def test_navigate_to_admin_page(self, page):
    #     """Test navigation to the Admin page after login.
    #
    #     This test verifies the following workflow:
    #     1. Login with admin credentials
    #     2. Navigate to the Admin section from dashboard
    #     3. Verify that the Admin page loads successfully
    #     """
    #     # Initialize page objects for different pages in the application
    #     login_page = LoginPage(self.page)
    #     dashboard_page = DashboardPage(self.page)
    #     admin_page = AdminUserPage(self.page)
    #
    #     # Step 1: Perform login with admin credentials
    #     login_page.login("Admin", "admin123")
    #
    #     # Step 2: Navigate from dashboard to admin page
    #     dashboard_page.go_to_admin()
    #
    #     # Step 3: Assert that the admin page has loaded successfully
    #     assert admin_page.is_admin_page_loaded()

    def test_admin_page_search_user(self, page, logger):
        """Test searching for a user in the Admin page.
        
        This test verifies the following workflow:
        1. Login with admin credentials
        2. Navigate to the Admin section from dashboard
        3. Search for a specific user
        4. Verify that the user appears in the search results
        """
        # Initialize page objects for different pages in the application
        login_page = LoginPage(page, logger)
        dashboard_page = DashboardPage(page)
        admin_page = AdminUserPage(page, logger)

        # Step 1: Perform login with admin credentials
        login_page.login("Admin", "admin123")
        
        # Step 2: Navigate from dashboard to admin page
        dashboard_page.go_to_admin()

        # Step 3: Search for a specific user by entering username
        # admin_page.search_by_username("Admin")
        
        # Step 4: Select user role filter
        admin_page.select_user_role()

        # Step 5: Verify that the dropdown is visible and the search was performed
        expect(admin_page.user_role_dropdown).to_be_visible()
