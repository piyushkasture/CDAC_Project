from pages.BasePage import BasePage


class LoginPage(BasePage):

    Username = "input[name='username']"
    Password = "input[name='password']"
    LoginButton = "button[type='submit']"
    ErrorMssg = ".oxd-alert-content-text"

    def login(self, username, password):
        self.fill(self.Username, username)
        self.fill(self.Password, password)
        self.click(self.LoginButton)

    def get_error_message(self):
        return self.get_text(self.ErrorMssg)
