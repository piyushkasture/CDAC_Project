from playwright.sync_api import Page
from pages.BasePage import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        # self.todo_input = page.get_by_placeholder("What needs to be done?")
        super().__init__(page)
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.get_by_text("Invalid credentials")
        self.required_field = page.get_by_text("Required")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        return self.error_message.get_by_text("Invalid credentials")

    def get_required_field_message(self):
        return self.required_field.get_by_text("Required")