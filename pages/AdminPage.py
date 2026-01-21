from pages.BasePage import BasePage

class AdminPage(BasePage):

    ADMIN_HEADER = "//h6[text()='Admin']"
    USERNAME_SEARCH = "(//input[@class='oxd-input oxd-input--active'])[2]"
    SEARCH_BUTTON = "//button[@type='submit']"

    def is_admin_page_loaded(self):
        self.wait_for_element(self.ADMIN_HEADER)
        return self.is_visible(self.ADMIN_HEADER)

    def search_user(self, username):
        self.fill(self.USERNAME_SEARCH, username)
        self.click(self.SEARCH_BUTTON)
