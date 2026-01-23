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
        expect(dashboard_heading).to_be_visible()
        return dashboard_heading.is_visible()

    def go_to_admin(self):
        self.wait_for_element(self.AdminMenu)
        self.click(self.AdminMenu)

    def go_to_pim(self):
        self.click(self.PimMenu)

    def go_to_leave(self):
        self.wait_for_element(self.LeaveMenu)
        self.click(self.LeaveMenu)

    def go_to_recruitment(self):
        self.wait_for_element(self.RecruitmentMenu)
        self.click(self.RecruitmentMenu)