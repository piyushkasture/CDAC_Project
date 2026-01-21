from pages.BasePage import BasePage

class PIMPage(BasePage):

    PIM_HEADER = "//h6[text()='PIM']"
    EMPLOYEE_NAME_INPUT = "//input[@placeholder='Type for hints...']"
    SEARCH_BUTTON = "//button[@type='submit']"

    def is_pim_page_loaded(self):
        self.wait_for_element(self.PIM_HEADER)
        return self.is_visible(self.PIM_HEADER)

    def search_employee(self, name):
        self.fill(self.EMPLOYEE_NAME_INPUT, name)
        self.click(self.SEARCH_BUTTON)
