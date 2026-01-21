from playwright.sync_api import sync_playwright


class DriverManager:
    def __init__(self, browser_name="chromium", headless=False):
        self.browser_name = browser_name
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def start(self):
        self.playwright = sync_playwright().start()

        if self.browser_name == "firefox":
            self.browser = self.playwright.firefox.launch(headless=self.headless)
        elif self.browser_name == "egde":
            self.browser = self.playwright.chromium.launch(
                channel="msedge", headless=self.headless
            )
        else:
            self.browser = self.playwright.chromium.launch(headless=self.headless)

        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        return self.page

    def stop(self):
        if self.page:
            self.context.close()
            self.browser.close()
            self.playwright.stop()
