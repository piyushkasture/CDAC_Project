from playwright.sync_api import Page, expect
from utils.CustomLogger import get_logger


class BuzzPage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger("BuzzPage")
        self.logger.info("Initializing BuzzPage")


        # Post elements
        self.post_textarea = page.get_by_role("textbox", name="What's on your mind?")

        # Post button
        self.post_button = page.locator(
            "button.oxd-button--main:has-text('Post')"
        )

        self.share_photos_btn = page.get_by_role("button", name="Share Photos")
        self.file_input = page.get_by_role("button", name="Share Video")

        # Feed elements
        self.posts = page.locator("div.orangehrm-buzz-post")
        self.like_button = page.locator("button[aria-label='Like']")
        self.comment_button = page.locator("button[aria-label='Comment']")
        self.comment_input = page.get_by_placeholder("Write your comment...")

        # Common messages
        self.required_msg = page.locator("text=Required")
        self.delete_option = page.locator("text=Delete")

        # Menu icon
        self.first_post = page.locator(".oxd-buzz-post").first
        self.click_menu_icon = self.first_post.locator(".orangehrm-buzz-post-actions > button")

        menu = page.get_by_role("menu")
        self.edit_icon = menu.get_by_role("listitem").filter(has=page.get_by_text("Edit Post", exact=True))
        self.delete_icon = menu.get_by_role("listitem").filter(has=page.get_by_text("Delete Post", exact=True))

        # Like

        self.like_button = self.first_post.locator("#heart-svg")

        self.like_true = page.locator("button[aria-pressed='true']")

        # Comment
        self.comment_icon = self.first_post.locator(".orangehrm-buzz-post-actions > button")

  
    # Post Actions
  
    def create_text_post(self):
        # Create a buzz post with text content
        self.logger.info("Creating text post")
        self.post_textarea.click()
        self.logger.info("Post textarea clicked")

        self.post_textarea.fill("Hi, my name is Automation")
        self.logger.info("Post text entered")
        expect(self.post_button).to_be_visible()
        expect(self.post_button).to_be_enabled()
        self.post_button.click()
        self.logger.info("Post submitted")

    def create_buzz_post_with_max_characters(self):
        # Create post with maximum character limit
        self.logger.info("Creating buzz post with maximum characters")
        self.post_textarea.click()
        self.logger.info("Post textarea clicked")
        long_text = "Buzz Automation " * 20
        self.post_textarea.fill(long_text)
        self.logger.info(f"Max length text entered: {len(long_text)} characters")
        expect(self.post_button).to_be_visible()
        expect(self.post_button).to_be_enabled()
        self.post_button.click()
        self.logger.info("Max character post submitted")

    def create_buzz_post_with_empty(self):
        # Attempt to create post with empty content
        self.logger.info("Attempting to create post with empty content")
        self.post_textarea.click()
        self.logger.info("Post textarea clicked")
        self.post_textarea.fill("")
        self.logger.info("Empty content filled")
        expect(self.post_button).to_be_visible()
        expect(self.post_button).to_be_enabled()
        self.post_button.click()
        self.logger.info("Empty post submission attempted")

    def create_buzz_post_with_special_character(self):
        # Create post with special characters
        self.logger.info("Creating post with special characters")
        self.post_textarea.click()
        self.logger.info("Post textarea clicked")
        self.post_textarea.fill("@#$%#%^$#@@$#!%^&$&&")
        self.logger.info("Special character text entered")
        expect(self.post_button).to_be_visible()
        expect(self.post_button).to_be_enabled()
        self.post_button.click()
        self.logger.info("Special character post submitted")

    def create_post_with_image(self, image_path: str, text: str):
        # Create post with image attachment
        self.logger.info(f"Creating post with image: {image_path}")
        self.share_photos_btn.click()
        self.logger.info("Share Photos button clicked")
        self.file_input.set_input_files(image_path)
        self.logger.info(f"Image file selected: {image_path}")
        self.post_textarea.fill(text)
        self.logger.info(f"Post text entered: {text}")
        self.post_button.click()
        self.logger.info("Image post submitted")

    def submit_empty_post(self):
        # Attempt to submit post without content
        self.logger.info("Attempting to submit empty post")
        self.post_button.click()
        self.logger.info("Empty post submission attempted")

  
    # Validation Helpers
  
    def is_post_visible(self, text):
        # Check if post with specific text is visible
        self.logger.info(f"Checking if post visible: {text}")
        result = self.page.locator(f"text={text}").is_visible()
        self.logger.info(f"Post visibility status: {result}")
        return result

    def is_post_text_visible(self, text):
        # Verify post text element visibility
        self.logger.info(f"Verifying post text visibility: {text}")
        result = self.page.locator(
            ".orangehrm-buzz-post-body-text, .oxd-buzz-post-body-text",
            has_text=text
        ).first
        self.logger.info(f"Post text element found: {result is not None}")
        return result

    def is_post_visible_for_max_characters(self):
        # Verify post with maximum characters is visible
        self.logger.info("Verifying max character post visibility")
        result = self.page.locator(
                ".orangehrm-buzz-post-body-text, .oxd-buzz-post-body-text"
            ).first
        self.logger.info("Max character post element located")
        return result

    def is_post_with_partial_text(self, text):
        # Verify post with partial text match
        self.logger.info(f"Checking post with partial text: {text[:3]}")
        result = self.page.locator(
            ".orangehrm-buzz-post-body-text, .oxd-buzz-post-body-text",
            has_text=text[:3]  # partial match
        ).first
        self.logger.info("Partial text post located")
        return result

    def is_required_message_visible(self):
        # Check if required field validation message is visible
        self.logger.info("Checking required message visibility")
        result = self.required_msg.is_visible()
        self.logger.info(f"Required message visible: {result}")
        return result

  
    # Like Actions

    # def like_button_first_post(self):
    #     post = self.page.locator(".oxd-buzz-post").first
    #     post.hover()
    #     return post.locator(".orangehrm-buzz-post-actions button").first

    def like_first_post(self):
        # Like the first post in the feed
        self.logger.info("Liking first post")
        post = self.page.locator(".oxd-buzz-post").first
        post.hover()
        self.logger.info("Post element hovered")

        btn = post.locator(".orangehrm-buzz-post-actions button").first
        expect(btn).to_be_visible()
        btn.click()
        self.logger.info("Like button clicked")

    def like_count_first_post(self) -> int:
        # Get like count from first post
        self.logger.info("Retrieving like count from first post")
        post = self.page.locator(".oxd-buzz-post").first

        # Like count text (may NOT exist if count = 0)
        like_text = post.locator(".orangehrm-buzz-stats span")

        if like_text.count() == 0:
            self.logger.info("No likes found, returning 0")
            return 0

        text = like_text.first.inner_text().strip()
        # Examples: "1 Like", "2 Likes"
        count = int(text.split()[0])
        self.logger.info(f"Like count retrieved: {count}")
        return count

    # Comment Actions
  
    def add_comment_to_first_post(self):
        # Add comment to first post in feed
        self.logger.info("Adding comment to first post")
        self.comment_icon.first.click()
        self.logger.info("Comment icon clicked")
        self.comment_input.fill("Nice post")
        self.logger.info("Comment text entered")
        self.page.keyboard.press("Enter")
        self.logger.info("Comment submitted")

    def submit_empty_comment(self):
        # Attempt to submit empty comment
        self.logger.info("Attempting to submit empty comment")
        self.comment_button.first.click()
        self.logger.info("Comment button clicked")
        self.comment_input.fill("")
        self.logger.info("Empty comment content filled")
        self.page.keyboard.press("Enter")
        self.logger.info("Empty comment submission attempted")

  
    # Delete Actions
  
    def delete_own_post(self, post_text: str):
        # Delete a post by post text
        self.logger.info(f"Deleting post with text: {post_text}")
        post = self.page.locator(f"text={post_text}")
        post.locator("..").locator("button").click()
        self.logger.info("Post menu button clicked")
        self.delete_option.click()
        self.logger.info("Post deleted")

    def is_delete_option_visible(self):
        # Check if delete option is visible in post menu
        self.logger.info("Checking delete option visibility")
        result = self.delete_option.is_visible()
        self.logger.info(f"Delete option visible: {result}")
        return result
  
    def get_post_count(self):
        # Get count of posts in feed
        self.logger.info("Retrieving post count from feed")
        count = self.posts.count()
        self.logger.info(f"Total posts in feed: {count}")
        return count
