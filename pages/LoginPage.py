from playwright.sync_api import Page
from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page, logger=None):
        # self.todo_input = page.get_by_placeholder("What needs to be done?")
        super().__init__(page)
        self.logger = logger

        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator(".oxd-alert-content-text")
        self.required_field = page.locator(".oxd-input-field-error-message")

    def login(self, username, password):

        self.logger.info(f"Attempting to login with username: {username} and password: {password}")
        
        self.username_input.fill(username)
        self.logger.info("Entering username")

        self.password_input.fill(password)
        self.logger.info("Entering password")

        self.login_button.click()
        self.logger.info("Click on login button")

    def get_error_message(self):
        return self.error_message

    def get_required_field_message(self):
        return self.required_field.first