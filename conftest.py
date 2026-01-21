import os
import yaml
import pytest
from utils.DriverManager import DriverManager


@pytest.fixture(params=["chromium", "firefox"], scope="function")
def setup_and_teardown(request):
    browser = request.param

    config_path = os.path.join("config", "environments", "dev.yaml")
    with open(config_path) as f:
        config = yaml.safe_load(f)

    driver = DriverManager(browser_name=browser, headless=False)
    page = driver.start()

    page.goto(config["url"])
    request.cls.page = page

    yield

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshot_path = f"reports/screenshots/{browser}_{request.node.name}.png"
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        page.screenshot(path=screenshot_path)

    driver.stop()


def pytest_runtest_makereport(item, call):
    if call.when == "call":
        item.rep_call = call

