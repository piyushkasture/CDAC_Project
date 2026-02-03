from pages.ProfilePage import ProfilePage
from playwright.sync_api import expect
from utils.base_test import BaseTest
from utils.CustomLogger import get_logger


class TestProfile(BaseTest):

    def test_logout(self,logger, profile_page):
        # Test: Verify user logout redirects to login page
        logger = get_logger("test_logout")
        profile = ProfilePage(profile_page)
        logger.info("Clicking logout button")
        profile.click_logout_button()
        logger.info("Verifying redirect to login page")
        expect(profile_page).to_have_url(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )
        logger.info("Logout validation passed")
