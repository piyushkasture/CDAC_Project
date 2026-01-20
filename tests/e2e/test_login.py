
from utils.base_test import BaseTest


class TestLogin(BaseTest):
    def test_login(self):
        self.page.fill("Admin", "admin123")
