import yaml
import os
import pytest
from DriverManager import DriverManager


@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:
    page = None



@pytest.fixture(scope="function")
def setup_and_teardown(request):
    config_path = os.path.join("config", "environments", "dev.yaml")

    with open(config_path) as file:
        config = yaml.safe_load(file)

    page = DriverManager.get_page(
        browser_name=config.get("browser"),
        headless=False
    )

    page.goto(config.get("url"))
    request.cls.page = page

    yield

    if request.node.rep_call.failed:
        screenshot_path = f"reports/screenshots/{request.node.name}.png"
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        page.screenshot(path=screenshot_path)

    DriverManager.quit_browser()


def pytest_runtest_makereport(item, call):
    if call.when == "call":
        item.rep_call = call

