from pages.ProfilePage import ProfilePage
from playwright.sync_api import expect
from utils.base_test import BaseTest


class TestProfile(BaseTest):

    def test_logout(self,page, profile_page):
        profile = ProfilePage(profile_page)
        profile.click_logout_button()
        page.wait_for_timeout(60000)

        expect(profile_page).to_have_url(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )
