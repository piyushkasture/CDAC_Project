from pathlib import Path
import os
import yaml
import pytest
import allure
from slugify import slugify
from utils.DriverManager import DriverManager
from utils.CustomLogger import get_logger

@pytest.fixture
def logger(request):
    # Initialize logger for the test with the test name for better tracking
    return get_logger(request.node.name)

# Browser + Page Setup

@pytest.fixture(scope="function", params=["chromium"])
def page(request, logger):
    # Get the browser type from parametrized test
    browser = request.param
    
    # Create logger for browser setup
    logger = get_logger("browser_setup")
    logger.info(f"Starting browser setup with browser type: {browser}")

    # Load configuration from YAML file for the current environment
    config_path = os.path.join("config", "environments", "dev.yaml")
    with open(config_path) as f:
        config = yaml.safe_load(f)
    logger.info(f"Configuration loaded from {config_path}")

    # Initialize the browser driver with specified browser type
    driver = DriverManager(browser_name=browser, headless=False)
    logger.info(f"DriverManager initialized for {browser}")
    
    page = driver.start()
    logger.info(f"Browser started successfully")

    # Set global timeout and navigate to the application URL
    page.set_default_timeout(60000)
    logger.info(f"Default timeout set to 60000ms")
    
    logger.info(f"Navigating to url: {config['url']}")

    page.goto(config["url"], wait_until="load")
    logger.info(f"Navigation completed successfully")

    # Yield page to test, cleanup happens after test completes
    yield page

    # Browser close happens AFTER screenshots
    logger.info(f"Closing browser and cleaning up resources")
    driver.stop()
    logger.info(f"Browser cleanup completed")


# Screenshot + Reporting Hook
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Create logger for reporting
    report_logger = get_logger("test_report")
    
    # Get the HTML plugin for pytest to attach screenshots
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    
    report_logger.info(f"Test report generated for: {item.nodeid}")

    # Only capture screenshots after test execution (not during setup/teardown)
    if report.when == "call":
        report_logger.info(f"Test execution phase: {report.when}")
        
        # Ensure Playwright page is available
        if hasattr(item, "funcargs") and "page" in item.funcargs:
            page = item.funcargs["page"]
            report_logger.info(f"Page object found, proceeding with screenshot capture")

            try:
                # Create screenshots directory if it doesn't exist
                screenshot_dir = Path("reports/screenshots")
                screenshot_dir.mkdir(parents=True, exist_ok=True)
                report_logger.info(f"Screenshot directory created/verified at {screenshot_dir}")

                # Generate screenshot filename based on test name
                file_name = f"{slugify(item.nodeid)}.png"
                screen_file = screenshot_dir / file_name
                report_logger.info(f"Screenshot filename generated: {file_name}")

                # Take screenshot of the current page state
                page.screenshot(path=str(screen_file))
                report_logger.info(f"Screenshot captured successfully")

                # Determine test status for screenshot naming
                if report.passed:
                    status = "Pass"
                    report_logger.info(f"Test PASSED")
                elif report.failed:
                    status = "Failure"
                    report_logger.warning(f"Test FAILED")
                elif report.skipped:
                    status = "Skipped"
                    report_logger.info(f"Test SKIPPED")
                else:
                    status = "Screenshot"
                    report_logger.info(f"Test status: {status}")

                # Attach screenshot to pytest-html report
                if pytest_html:
                    extra.append(pytest_html.extras.png(str(screen_file)))
                    report_logger.info(f"Screenshot attached to pytest-html report")

                # Attach screenshot to Allure report for better visibility
                allure.attach.file(
                    str(screen_file),
                    name=f"{status} Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
                report_logger.info(f"Screenshot attached to Allure report with status: {status}")

            except Exception as e:
                # Log any errors that occur during screenshot capture
                report_logger.error(f"Screenshot capture failed: {str(e)}")
                print(f"Screenshot capture failed: {e}")
        else:
            report_logger.warning(f"Page object not found in test fixtures")

        # Attach all collected extras to the report
        report.extra = extra
        report_logger.info(f"Report finalized with {len(extra)} extra attachments")
