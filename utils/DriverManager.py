from playwright.sync_api import sync_playwright

#  Handles browser initialization, context creation, and cleanup
class DriverManager:
    def __init__(self, browser_name="chromium", headless=False):
        # Initialize DriverManager with specified browser configuration.
        
        self.browser_name = browser_name # Browser type: 'chromium'
        self.headless = headless      # Headless mode false
        self.playwright = None  # Playwright instance
        self.browser = None     # Browser instance
        self.context = None     # Browser context
        self.page = None        # Page instance used for test interactions

    def start(self):
        # Launch the browser
        
        # Initialize Playwright
        self.playwright = sync_playwright().start()

        # Launch the browser based on browser_name parameter 
        if self.browser_name == "firefox":
            self.browser = self.playwright.firefox.launch(headless=self.headless)
        elif self.browser_name == "edge":
            self.browser = self.playwright.chromium.launch(
                channel="msedge", headless=self.headless
            )
        else:
            # Default to Chromium browser
            self.browser = self.playwright.chromium.launch(headless=self.headless)

        # Create a new browser context for test isolation
        self.context = self.browser.new_context()
        # Create a new page
        self.page = self.context.new_page()
        return self.page

    def stop(self):
        # Stop the browser and Playwright instance
        if self.page:
            # Close the browser context
            self.context.close()
            # Close the browser instance
            self.browser.close()
            # Stop the Playwright instance
            self.playwright.stop()
