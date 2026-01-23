from pathlib import Path
import os
import yaml
import pytest
import allure
from slugify import slugify
from utils.DriverManager import DriverManager


# Browser + Page Setup

@pytest.fixture(scope="function", params=["chromium"])
def page(request):
    browser = request.param

    config_path = os.path.join("config", "environments", "dev.yaml")
    with open(config_path) as f:
        config = yaml.safe_load(f)

    driver = DriverManager(browser_name=browser, headless=False)
    page = driver.start()

    page.set_default_timeout(60000)
    page.goto(
        config["url"],
        wait_until="domcontentloaded",
        timeout=60000
    )

    yield page

    # Browser close happens AFTER screenshots
    driver.stop()


# Screenshot + Reporting Hook
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call":
        # Ensure Playwright page is available
        if hasattr(item, "funcargs") and "page" in item.funcargs:
            page = item.funcargs["page"]

            try:
                screenshot_dir = Path("reports/screenshots")
                screenshot_dir.mkdir(parents=True, exist_ok=True)

                file_name = f"{slugify(item.nodeid)}.png"
                screen_file = screenshot_dir / file_name

                page.screenshot(path=str(screen_file))

                # Status naming
                if report.passed:
                    status = "Pass"
                elif report.failed:
                    status = "Failure"
                elif report.skipped:
                    status = "Skipped"
                else:
                    status = "Screenshot"

                # Attach to pytest-html
                if pytest_html:
                    extra.append(pytest_html.extras.png(str(screen_file)))

                # Attach to Allure
                allure.attach.file(
                    str(screen_file),
                    name=f"{status} Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            except Exception as e:
                print(f"Screenshot capture failed: {e}")

        report.extra = extra
