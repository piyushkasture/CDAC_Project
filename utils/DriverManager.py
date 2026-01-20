from playwright.sync_api import sync_playwright


class DriverManager:
    _playwright = None
    _browser = None
    _context = None
    _page = None

    @classmethod
    def get_page(cls, browser_name="chromium", headless=False):
        if cls._page is None:
            cls._playwright = sync_playwright().start()

            if browser_name == "firefox":
                cls._browser = cls._playwright.firefox.launch(headless=headless)
            elif browser_name == "edge":
                cls._browser = cls._playwright.chromium.launch(channel="msedge", headless=headless)
            else:
                cls._browser = cls._playwright.chromium.launch(headless=headless)

            cls._context = cls._browser.new_context()
            cls._page = cls._context.new_page()

        return cls._page

    @classmethod
    def quit_browser(cls):
        if cls._page:
            cls._context.close()
            cls._browser.close()
            cls._playwright.stop()

            cls._page = None
            cls._context = None
            cls._browser = None
            cls._playwright = None
