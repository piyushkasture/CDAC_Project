from utils.CustomLogger import get_logger

class BasePage:
    def __init__(self, page, logger=None):
        self.page = page
        self.logger = logger or get_logger(self.__class__.__name__)

    def wait_for_element(self, locator, timeout=5000):
        # Wait for an element to be present on the page before proceeding.
        self.page.locator(locator).wait_for(timeout=timeout)
