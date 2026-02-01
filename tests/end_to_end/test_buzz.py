import pytest
from playwright.sync_api import Page, expect

# @pytest.mark.buzz
class TestBuzzModule:

    def test_to_test_loading_of_buzz_page(self, page: Page, login):
        page.click("text=Buzz")
        expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz")
        expect(page.locator("textarea")).to_be_visible()

    def test_to_test_visibility_of_ui_elements_on_buzz_page(self, page: Page, login):
        page.click("text=Buzz")
        expect(page.locator("textarea")).to_be_visible()
        expect(page.locator("text=Share Photos")).to_be_visible()
        expect(page.locator("button:has-text('Post')")).to_be_visible()

    def test_to_test_creating_text_only_buzz_post(self, page: Page, login):
        page.click("text=Buzz")
        page.fill("textarea", "Automation test Buzz post")
        page.click("button:has-text('Post')")
        expect(page.locator("text=Automation test Buzz post")).to_be_visible()

    def test_to_test_creating_buzz_post_with_max_characters(self, page: Page, login):
        page.click("text=Buzz")
        long_text = "Buzz Automation " * 20
        page.fill("textarea", long_text)
        page.click("button:has-text('Post')")
        expect(page.locator(f"text={long_text[:20]}")).to_be_visible()

    def test_to_test_submitting_empty_buzz_post(self, page: Page, login):
        page.click("text=Buzz")
        page.click("button:has-text('Post')")
        expect(page.locator("text=Required")).to_be_visible()

    def test_to_test_buzz_post_with_special_characters(self, page: Page, login):
        page.click("text=Buzz")
        special_text = "!@#$%^&*()_+"
        page.fill("textarea", special_text)
        page.click("button:has-text('Post')")
        expect(page.locator(f"text={special_text}")).to_be_visible()

    def test_to_test_posting_with_image_upload(self, page: Page, login):
        page.click("text=Buzz")
        page.click("text=Share Photos")
        page.set_input_files(
            "input[type='file']",
            "tests/test_data/sample_image.png"
        )
        page.fill("textarea", "Post with image")
        page.click("button:has-text('Post')")
        expect(page.locator("img")).to_be_visible()

    def test_to_test_invalid_file_upload_in_buzz_post(self, page: Page, login):
        page.click("text=Buzz")
        page.click("text=Share Photos")
        page.set_input_files(
            "input[type='file']",
            "tests/test_data/invalid_file.pdf"
        )
        expect(page.locator("text=File type not allowed")).to_be_visible()

    def test_to_test_liking_a_buzz_post(self, page: Page, login):
        page.click("text=Buzz")
        page.locator("button[aria-label='Like']").first.click()
        expect(page.locator("button[aria-pressed='true']")).to_be_visible()

    def test_to_test_adding_comment_to_buzz_post(self, page: Page, login):
        page.click("text=Buzz")
        page.locator("button[aria-label='Comment']").first.click()
        page.fill("input[placeholder='Write your comment...']", "Nice post")
        page.keyboard.press("Enter")
        expect(page.locator("text=Nice post")).to_be_visible()

    def test_to_test_empty_comment_submission(self, page: Page, login):
        page.click("text=Buzz")
        page.locator("button[aria-label='Comment']").first.click()
        page.keyboard.press("Enter")
        expect(page.locator("text=Required")).to_be_visible()

    def test_to_test_deleting_own_buzz_post(self, page: Page, login):
        page.click("text=Buzz")
        page.fill("textarea", "Post to delete")
        page.click("button:has-text('Post')")
        page.locator("text=Post to delete").locator("..").locator("button").click()
        page.click("text=Delete")
        expect(page.locator("text=Post to delete")).not_to_be_visible()

    def test_to_test_restriction_on_deleting_others_buzz_posts(self, page: Page, login):
        page.click("text=Buzz")
        expect(page.locator("text=Delete")).not_to_be_visible()

    # def test_to_test_buzz_access_after_logout(self, page: Page, login):
    #     page.click("text=Logout")
    #     page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz")
    #     expect(page).to_have_url(/auth\/login/)

    def test_to_test_creating_multiple_buzz_posts_sequentially(self, page: Page, login):
        page.click("text=Buzz")
        posts = ["Post 1", "Post 2", "Post 3"]
        for post in posts:
            page.fill("textarea", post)
            page.click("button:has-text('Post')")
            expect(page.locator(f"text={post}")).to_be_visible()

    def test_to_test_buzz_module_access_based_on_user_roles(self, page: Page, login):
        page.click("text=Buzz")
        expect(page.locator("textarea")).to_be_visible()
