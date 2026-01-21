from pages.BasePage import BasePage


class DashboardPage(BasePage):

    DASHBOARD_HEADER = "//h6[text()='Dashboard']"
    ADMIN_MENU = "//span[text()='Admin']"
    PIM_MENU = "//span[text()='PIM']"

    def is_dashboard_visible(self):
        self.wait_for_element(self.DASHBOARD_HEADER)
        return self.is_visible(self.DASHBOARD_HEADER)

    def go_to_admin(self):
        self.wait_for_element(self.ADMIN_MENU)
        self.click(self.ADMIN_MENU)

    def go_to_pim(self):
        self.click(self.PIM_MENU)
