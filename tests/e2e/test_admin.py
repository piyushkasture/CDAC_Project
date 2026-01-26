from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from utils.base_test import BaseTest
from pages.AdminPage import AdminPage


class TestAdmin(BaseTest):
    """
    Test class for Admin page functionality.
    Tests admin-related features and navigation in the OrangeHRM application.
    """

    def test_navigate_to_admin_page(self):
        """Test navigation to the Admin page after login.
        
        This test verifies the following workflow:
        1. Login with admin credentials
        2. Navigate to the Admin section from dashboard
        3. Verify that the Admin page loads successfully
        """
        # Initialize page objects for different pages in the application
        login_page = LoginPage(self.page)
        dashboard_page = DashboardPage(self.page)
        admin_page = AdminPage(self.page)

        # Step 1: Perform login with admin credentials
        login_page.login("Admin", "admin123")
        
        # Step 2: Navigate from dashboard to admin page
        dashboard_page.go_to_admin()

        # Step 3: Assert that the admin page has loaded successfully
        assert admin_page.is_admin_page_loaded()
