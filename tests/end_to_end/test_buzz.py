from playwright.sync_api import expect
from pages.BuzzPage import BuzzPage
from utils.CustomLogger import get_logger

class TestBuzz:

    def test_loading_of_buzz_page(self,logger, buzz_page):
        # Test: Verify Buzz page loads with correct URL
        logger = get_logger("test_loading_of_buzz_page")
        BuzzPage(buzz_page)
        logger.info("Verifying Buzz page URL")
        expect(buzz_page).to_have_url(
            "https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz"
        )
        logger.info("Buzz page URL verified successfully")

    def test_creating_text_only_buzz_post(self,logger, buzz_page):
        # Test: Create a text-only buzz post and verify visibility
        logger = get_logger("test_creating_text_only_buzz_post")
        buzz = BuzzPage(buzz_page)
        logger.info("Creating text-only buzz post")
        buzz.create_text_post()
        logger.info("Verifying text post visibility")
        expect(buzz.is_post_text_visible("Hi, my name is Automation")).to_be_visible()
        logger.info("Text post created and verified successfully")

    def test_creating_buzz_post_with_max_characters(self,logger, buzz_page):
        # Test: Create buzz post with maximum allowed characters
        logger = get_logger("test_creating_buzz_post_with_max_characters")
        buzz = BuzzPage(buzz_page)
        logger.info("Creating buzz post with max characters")
        buzz.create_buzz_post_with_max_characters()
        logger.info("Verifying max character post visibility")
        expect(buzz.is_post_visible_for_max_characters()).to_be_visible()
        logger.info("Max character post created and verified successfully")

    def test_submitting_empty_buzz_post(self,logger, buzz_page):
        # Test: Verify empty buzz post cannot be submitted
        logger = get_logger("test_submitting_empty_buzz_post")
        buzz = BuzzPage(buzz_page)
        logger.info("Getting post count before empty submission")
        before = buzz.get_post_count()
        logger.info(f"Post count before: {before}")
        logger.info("Attempting to create empty buzz post")
        buzz.create_buzz_post_with_empty()
        after = buzz.get_post_count()
        logger.info(f"Post count after: {after}")
        assert before == after
        logger.info("Empty post submission validation passed")

    def test_buzz_post_with_special_characters(self,logger, buzz_page):
        # Test: Create buzz post with special characters
        logger = get_logger("test_buzz_post_with_special_characters")
        buzz = BuzzPage(buzz_page)
        logger.info("Creating buzz post with special characters")
        buzz.create_buzz_post_with_special_character()
        logger.info("Verifying special character post visibility")
        expect(buzz.is_post_with_partial_text("@#$%#%^$#@@$#!%^&$&&")).to_be_visible()
        logger.info("Special character post created and verified successfully")


    # def test_liking_a_buzz_post(self,logger, buzz_page):
    #     # Test: Like a buzz post and verify like count increases
    #     logger = get_logger("test_liking_a_buzz_post")
    #     buzz = BuzzPage(buzz_page)
    #     logger.info("Getting like count before liking")
    #     count_before = buzz.like_count_first_post()
    #     logger.info(f"Like count before: {count_before}")
    #     logger.info("Liking first post")
    #     buzz.like_first_post()
    #     buzz_page.wait_for_timeout(1000)
    #     logger.info("Getting like count after liking")
    #     count_after = buzz.like_count_first_post()
    #     logger.info(f"Like count after: {count_after}")
    #     assert count_after == count_before + 1
    #     logger.info("Like count validation passed")
    #
    # def test_adding_comment_to_buzz_post(self,logger, buzz_page):
    #     # Test: Add comment to first buzz post and verify visibility
    #     logger = get_logger("test_adding_comment_to_buzz_post")
    #     buzz = BuzzPage(buzz_page)
    #     logger.info("Adding comment to first post")
    #     buzz.add_comment_to_first_post()
    #     logger.info("Verifying comment visibility")
    #     expect(buzz.is_post_visible("Nice post")).to_be_visible()
    #     logger.info("Comment added and verified successfully")
    #
    # def test_empty_comment_submission(self,logger, buzz_page):
    #     # Test: Verify empty comment cannot be submitted
    #     logger = get_logger("test_empty_comment_submission")
    #     buzz = BuzzPage(buzz_page)
    #     logger.info("Attempting to submit empty comment")
    #     buzz.submit_empty_comment()
    #     logger.info("Verifying page still visible after empty submission")
    #     expect(buzz_page).to_be_visible()
    #     logger.info("Empty comment submission validation passed")

    # def test_restriction_on_deleting_others_buzz_posts(self, buzz_page):
    #     # Test: Verify cannot delete other user's buzz posts
    #     logger = get_logger("test_restriction_on_deleting_others_buzz_posts")
    #     buzz = BuzzPage(buzz_page)
    #     logger.info("Clicking menu icon on buzz post")
    #     buzz.click_menu_icon.click()
    #     logger.info("Verifying delete option is not visible for other's post")
