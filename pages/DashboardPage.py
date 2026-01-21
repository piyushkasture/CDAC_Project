from pages.BasePage import BasePage


class DashboardPage(BasePage):

    DASHBOARD_HEADER = "//h6[text()='Dashboard']"
    ADMIN_MENU = "//span[text()='Admin']"
    PIM_MENU = "//span[text()='PIM']"
    LEAVE_MENU = "//span[text()='Leave']"
    RECRUITMENT_MENU = "//span[text()='Recruitment']"

    def is_dashboard_visible(self):
        self.wait_for_element(self.DASHBOARD_HEADER)
        return self.is_visible(self.DASHBOARD_HEADER)

    def go_to_admin(self):
        self.wait_for_element(self.ADMIN_MENU)
        self.click(self.ADMIN_MENU)

    def go_to_pim(self):
        self.click(self.PIM_MENU)

    def go_to_leave(self):
        self.wait_for_element(self.LEAVE_MENU)
        self.click(self.LEAVE_MENU)

    def go_to_recruitment(self):
        self.wait_for_element(self.RECRUITMENT_MENU)
        self.click(self.RECRUITMENT_MENU)