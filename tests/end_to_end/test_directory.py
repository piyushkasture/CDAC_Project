from playwright.sync_api import expect
from pages.DirectoryPage import DirectoryPage
from utils.CustomLogger import get_logger

class TestDirectory:

    def test_search_employee_by_name(self,logger, directory_page):
        # Test: Search employee by name and verify results
        logger = get_logger("test_search_employee_by_name")
        directory = DirectoryPage(directory_page)
        logger.info("Searching for employee by name")
        directory.search_employee_by_name()
        logger.info("Verifying employee card is visible")
        expect(directory.employee_cards.first).to_be_visible()
        logger.info("Employee name search passed")

    def test_search_employee_by_invalid_name(self,logger, directory_page):
        # Test: Search with invalid name and verify no records found
        logger = get_logger("test_search_employee_by_invalid_name")
        directory = DirectoryPage(directory_page)
        logger.info("Searching for employee with invalid name")
        directory.search_employee_by_invalid_name()
        logger.info("Verifying no records found message")
        expect(directory.no_records_found).to_be_visible()
        logger.info("Invalid name search validation passed")

    def test_search_employee_by_job_title(self,logger, directory_page):
        # Test: Search employee by job title and verify results
        logger = get_logger("test_search_employee_by_job_title")
        directory = DirectoryPage(directory_page)
        logger.info("Searching for employee by job title")
        directory.search_employee_by_job_title()
        logger.info("Verifying employee card is visible")
        expect(directory.employee_cards.first).to_be_visible()
        logger.info("Job title search passed")

    def test_search_employee_by_location(self,logger, directory_page):
        # Test: Search employee by location and verify results
        logger = get_logger("test_search_employee_by_location")
        directory = DirectoryPage(directory_page)
        logger.info("Searching for employee by location")
        directory.search_employee_by_location()
        logger.info("Verifying employee card is visible")
        expect(directory.employee_cards.first).to_be_visible()
        logger.info("Location search passed")

    def test_search_employee_using_multiple_filters(self,logger, directory_page):
        # Test: Search employee using multiple filter criteria
        logger = get_logger("test_search_employee_using_multiple_filters")
        directory = DirectoryPage(directory_page)
        logger.info("Searching for employee using multiple filters")
        directory.search_employee_using_multiple_filters()
        logger.info("Verifying employee card is visible")
        expect(directory.employee_cards.first).to_be_visible()
        logger.info("Multiple filters search passed")

    def test_search_without_any_criteria(self,logger, directory_page):
        # Test: Search without entering any criteria shows all employees
        logger = get_logger("test_search_without_any_criteria")
        directory = DirectoryPage(directory_page)
        logger.info("Performing search without any criteria")
        directory.search_without_any_criteria()
        logger.info("Verifying employee cards are visible")
        expect(directory.employee_cards.first).to_be_visible()
        logger.info("No criteria search passed")

    def test_reset_button_functionality(self,logger, directory_page):
        # Test: Reset button clears all search filters
        logger = get_logger("test_reset_button_functionality")
        directory = DirectoryPage(directory_page)
        logger.info("Testing reset button functionality")
        directory.reset_button_functionality()
        logger.info("Verifying employee name input is empty after reset")
        expect(directory.employee_name_input).to_be_empty()
        logger.info("Reset button functionality passed")

    def test_multiple_consecutive_searches(self,logger, directory_page):
        # Test: Multiple consecutive searches work correctly
        logger = get_logger("test_multiple_consecutive_searches")
        directory = DirectoryPage(directory_page)
        logger.info("Performing multiple consecutive searches")
        directory.multiple_consecutive_searches()
        logger.info("Verifying employee card is visible")
        expect(directory.employee_cards.first).to_be_visible()
        logger.info("Multiple consecutive searches passed")

