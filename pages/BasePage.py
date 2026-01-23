from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def wait_for_element(self, locator, timeout=5000):
        self.page.locator(locator).wait_for(timeout=timeout)
