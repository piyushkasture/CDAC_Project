from playwright.sync_api import Page
from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page, logger=None):
        # Initialize LoginPage with page object and logger.

        super().__init__(page)
        self.logger = logger

        # Locators for login page elements
        self.username_input = page.get_by_placeholder("Username") # Username input field
        self.password_input = page.get_by_placeholder("Password") # Password input field
        self.login_button = page.get_by_role("button", name="Login") # Login button
        self.error_message = page.locator(".oxd-alert-content-text")  # Error message displayed on failed login
        self.required_field = page.locator(".oxd-input-field-error-message")  # Required field validation message

    def login(self, username, password):
        # Perform login action with given credentials.

        self.logger.info(f"Attempting to login with username: {username} and password: {password}")
        
        # Enter username
        self.username_input.fill(username)
        self.logger.info("Entering username")

        # Enter password
        self.password_input.fill(password)
        self.logger.info("Entering password")

        # Click login button
        self.login_button.click()
        self.logger.info("Click on login button")

    def get_error_message(self):
        # Get the error message element displayed after failed login attempt.
        return self.error_message

    def get_required_field_message(self):
        #Get the required field validation message element.

        return self.required_field.first # Return the first required field message element