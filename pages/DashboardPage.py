from pages.BasePage import BasePage


class DashboardPage(BasePage):


    def __init__(self, page):
        super().__init__(page)

        # Dashboard Locators

        # Dashboard heading
        self.dashboard_heading = page.get_by_role("heading", name="Dashboard")

        # User profile dropdown icon (top right)
        self.profile_icon = page.get_by_role("button").filter(
            has=page.locator("i.oxd-userdropdown-icon")
        )

        # Dashboard widgets
        self.widgets = page.locator("div.oxd-dashboard-widget")

        # Error
        self.error_message = page.locator(".oxd-alert-content-text")

        # Left menu items
        self.admin_menu = page.get_by_role("link", name="Admin")
        self.pim_menu = page.get_by_role("link", name="PIM")
        self.leave_menu = page.get_by_role("link", name="Leave")
        self.recruitment_menu = page.get_by_role("link", name="Recruitment")

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
