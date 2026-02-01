from playwright.sync_api import Page, expect


class BuzzPage:
    def __init__(self, page: Page):
        self.page = page

        # Navigation
        self.buzz_menu = page.locator("text=Buzz")

        # Post elements
        self.post_textarea = page.locator("textarea")
        self.post_button = page.locator("button:has-text('Post')")
        self.share_photos_btn = page.locator("text=Share Photos")
        self.file_input = page.locator("input[type='file']")

        # Feed elements
        self.posts = page.locator("div.orangehrm-buzz-post")
        self.like_button = page.locator("button[aria-label='Like']")
        self.comment_button = page.locator("button[aria-label='Comment']")
        self.comment_input = page.locator("input[placeholder='Write your comment...']")

        # Common messages
        self.required_msg = page.locator("text=Required")
        self.delete_option = page.locator("text=Delete")

    # ------------------------
    # Navigation Actions
    # ------------------------
    def open_buzz_page(self):
        self.buzz_menu.click()
        expect(self.post_textarea).to_be_visible()

    # ------------------------
    # Post Actions
    # ------------------------
    def create_text_post(self, text: str):
        self.post_textarea.fill(text)
        self.post_button.click()

    def create_post_with_image(self, image_path: str, text: str):
        self.share_photos_btn.click()
        self.file_input.set_input_files(image_path)
        self.post_textarea.fill(text)
        self.post_button.click()

    def submit_empty_post(self):
        self.post_button.click()

    # ------------------------
    # Validation Helpers
    # ------------------------
    def is_post_visible(self, text: str):
        return self.page.locator(f"text={text}").is_visible()

    def is_required_message_visible(self):
        return self.required_msg.is_visible()

    # ------------------------
    # Like Actions
    # ------------------------
    def like_first_post(self):
        self.like_button.first.click()

    # ------------------------
    # Comment Actions
    # ------------------------
    def add_comment_to_first_post(self, comment: str):
        self.comment_button.first.click()
        self.comment_input.fill(comment)
        self.page.keyboard.press("Enter")

    def submit_empty_comment(self):
        self.comment_button.first.click()
        self.page.keyboard.press("Enter")

    # ------------------------
    # Delete Actions
    # ------------------------
    def delete_own_post(self, post_text: str):
        post = self.page.locator(f"text={post_text}")
        post.locator("..").locator("button").click()
        self.delete_option.click()

    def is_delete_option_visible(self):
        return self.delete_option.is_visible()

    # ------------------------
    # Utility
    # ------------------------
    def get_post_count(self):
        return self.posts.count()
