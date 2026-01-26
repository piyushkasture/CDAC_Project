from playwright.sync_api import expect

from pages.BasePage import BasePage


class DashboardPage(BasePage):

    # DashboardHeader = "//h6[text()='Dashboard']"
    AdminMenu = "//span[text()='Admin']"
    PimMenu = "//span[text()='PIM']"
    LeaveMenu = "//span[text()='Leave']"
    RecruitmentMenu = "//span[text()='Recruitment']"

    def is_dashboard_visible(self):
        dashboard_heading = self.page.get_by_role("heading", name="Dashboard")
        return dashboard_heading

    def go_to_admin(self):
        self.wait_for_element(self.AdminMenu)
        self.page.locator(self.AdminMenu).click()

    def go_to_pim(self):
        self.page.locator(self.PimMenu).click()

    def go_to_leave(self):
        self.wait_for_element(self.LeaveMenu)
        self.page.locator(self.LeaveMenu).click()

    def go_to_recruitment(self):
        self.wait_for_element(self.RecruitmentMenu)
        self.page.locator(self.RecruitmentMenu).click()