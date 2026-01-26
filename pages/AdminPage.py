from logging import Logger

from playwright.sync_api import Page

from pages.BasePage import BasePage

class AdminUserPage(BasePage):
    def __init__(self, page: Page, logger=None):
        super().__init__(page)
        self.logger = logger

        # Locators
        self.username_input = page.locator("(//input[@class='oxd-input oxd-input--active'])[2]")
        # User role dropdown locator for selecting user roles
        self.user_role_dropdown = page.locator("(//div[@class='oxd-select-wrapper'])[1]")
        self.search_button = page.locator("//button[@type='submit']")

    # Method to fill username in search field
    def search_by_username(self, username):
        """Fill the username field with a value for searching.
        
        Args:
            username (str): Username to search for
        """
        self.username_input.fill(username)
        if self.logger:
            self.logger.info(f"Entered username for search: {username}")

    # Method to select user role from dropdown
    def select_user_role(self, role_index=1):
        """Select user role from the custom dropdown.
        
        Args:
            role_index (int): Index of the role option to select (default: 1)
        """
        # Click the dropdown to open it
        self.user_role_dropdown.click()
        # Wait for dropdown options to appear and click the desired option
        role_option = self.page.locator(f"(//div[@role='option'])[{role_index}]")
        role_option.click()
        if self.logger:
            self.logger.info(f"Selected user role at index: {role_index}")
        # Click search button to apply the filter
        self.search_button.click()

    # Method to get the selected value from the dropdown
    def get_selected_role(self):
        """Get the text of the currently selected role in the dropdown.
        
        Returns:
            str: The text of the selected role option
        """
        # Get the selected option text from the dropdown
        selected_value = self.page.locator("(//div[@class='oxd-select-wrapper'])[1]//span[@class='oxd-select-text--after']")
        return selected_value.text_content() if selected_value else None

    # AdminHeader = "//h6[text()='Admin']"
    # SearchUsername = "(//input[@class='oxd-input oxd-input--active'])[2]"
    # SearchButton = "//button[@type='submit']"
    #
    # def is_admin_page_loaded(self):
    #     self.wait_for_element(self.AdminHeader)
    #     return self.is_visible(self.AdminHeader)
    #
    def search_user(self, username):
        self.fill(self.username_input, username)
        self.click(self.search_button)