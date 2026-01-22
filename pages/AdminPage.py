from pages.BasePage import BasePage

class AdminPage(BasePage):

    AdminHeader = "//h6[text()='Admin']"
    SearchUsername = "(//input[@class='oxd-input oxd-input--active'])[2]"
    SearchButton = "//button[@type='submit']"

    def is_admin_page_loaded(self):
        self.wait_for_element(self.AdminHeader)
        return self.is_visible(self.AdminHeader)

    def search_user(self, username):
        self.fill(self.SearchUsername, username)
        self.click(self.SearchButton)
