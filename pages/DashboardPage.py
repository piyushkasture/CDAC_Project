import pytest

from pages.BasePage import BasePage

class DashboardPage(BasePage):


    def __init__(self, page):
        super().__init__(page)

        # Dashboard Locators

        # Dashboard heading
        self.dashboard_heading = page.get_by_role("heading", name="Dashboard")

        # User profile dropdown icon (top right)
        self.profile_icon = page.get_by_role("button").filter(has=page.locator("i.oxd-userdropdown-icon"))

        # Dashboard widgets
        self.widgets = page.locator("div.oxd-dashboard-widget")

        # Error
        self.error_message = page.locator(".oxd-alert-content-text")

        # Left menu items
        self.admin_menu = page.get_by_role("link", name="Admin")
        self.pim_menu = page.get_by_role("link", name="PIM")
        self.leave_menu = page.get_by_role("link", name="Leave")
        self.recruitment_menu = page.get_by_role("link", name="Recruitment")
        self.myInfo_menu = page.get_by_role("link", name="My Info")
        self.profile_button = (self.page.get_by_role("banner").get_by_alt_text("profile picture"))
        self.directory_menu = page.get_by_role("link", name="Directory")
        self.maintenance_menu = page.get_by_role("link", name="Maintenance")
        self.buzz_menu = page.get_by_role("link", name="Buzz")
        self.time_menu = page.get_by_role("link", name="Time")
        self.claim_menu = page.get_by_role("link", name="Claim")

    # Dashboard validations
    def is_dashboard_visible(self):
        return self.dashboard_heading

    def get_profile_icon(self):
        return self.profile_icon

    def get_widgets(self):
        return self.widgets

    def get_error_message(self):
        return self.error_message

    # Navigation actions
    def go_to_admin(self):
        self.admin_menu.click()

    def go_to_pim(self):
        self.pim_menu.click()

    def go_to_leave(self):
        self.leave_menu.click()

    def go_to_recruitment(self):
        self.recruitment_menu.click()

    def go_to_myinfo(self):
        self.myInfo_menu.click()

    def go_to_profile(self):
        self.profile_button.click()

    def go_to_directory(self):
        self.directory_menu.click()

    def go_to_maintenance(self):
        self.maintenance_menu.click()

    def go_to_buzz(self):
        self.buzz_menu.click()

    def go_to_time(self):
        self.time_menu.click()

    def go_to_claim(self):
        self.claim_menu.click()