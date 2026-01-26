from playwright.sync_api import Page


class BasePage:
    """
    Base page class that serves as the parent class for all page objects.
    This class encapsulates common functionality used across different pages
    such as waiting for elements and interacting with the page.
    """
    
    def __init__(self, page: Page):
        """Initialize BasePage with a Playwright page object.
        
        Args:
            page (Page): Playwright page instance for interacting with the web application
        """
        self.page = page

    def wait_for_element(self, locator, timeout=5000):
        """Wait for an element to be present on the page before proceeding.
        
        Args:
            locator (str): CSS or XPath locator of the element to wait for
            timeout (int): Maximum time in milliseconds to wait for the element (default: 5000ms)
        """
        self.page.locator(locator).wait_for(timeout=timeout)
