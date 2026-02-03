
from playwright.sync_api import expect
from pages.MaintenancePage import MaintenancePage
from utils.CustomLogger import get_logger

class TestMaintenance:

    def test_maintenance_access_with_invalid_password(self,logger,maintenance_page):
        # Test: Verify error message shown for invalid maintenance password
        logger = get_logger("test_maintenance_access_with_invalid_password")
        maintenance = MaintenancePage(maintenance_page)
        logger.info("Attempting maintenance access with invalid password")
        maintenance.open_maintenance_with_invalid_password()
        logger.info("Verifying error message is visible")
        expect(maintenance.error_message).to_be_visible()
        logger.info("Invalid password error validation passed")

    def test_maintenance_access_with_blank_password(self,logger, maintenance_page):
        # Test: Verify required message shown for blank password
        logger = get_logger("test_maintenance_access_with_blank_password")
        maintenance = MaintenancePage(maintenance_page)
        logger.info("Attempting maintenance access with blank password")
        maintenance.open_maintenance_with_black_password()
        logger.info("Verifying required message is visible")
        expect(maintenance.required_message).to_be_visible()
        logger.info("Blank password validation passed")

    def test_maintenance_access_with_valid_password(self,logger, maintenance_page):
        # Test: Verify maintenance access granted with valid password
        logger = get_logger("test_maintenance_access_with_valid_password")
        maintenance = MaintenancePage(maintenance_page)
        logger.info("Accessing maintenance module with valid password")
        maintenance.open_maintenance_with_valid_password()
        logger.info("Verifying maintenance page URL")
        expect(maintenance_page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/maintenance/purgeEmployee")
        logger.info("Valid password access validation passed")

    def test_loading_of_employee_records_page(self,logger, maintenance_page):
        # Test: Verify employee records page loads successfully
        logger = get_logger("test_loading_of_employee_records_page")
        maintenance = MaintenancePage(maintenance_page)
        logger.info("Opening employee records page")
        logger.info("Verifying employee records page heading is visible")
        expect(maintenance.landing_page_heading).to_be_visible()
        logger.info("Employee records page loaded successfully")

    def test_search_employee_records(self,logger, maintenance_page):
        # Test: Search past employee records and verify no records found
        logger = get_logger("test_search_employee_records")
        maintenance = MaintenancePage(maintenance_page)
        logger.info("Searching for past employee records")
        maintenance.search_past_employee_records()
        logger.info("Verifying no records found message")
        expect(maintenance.no_records_found).to_be_visible()
        logger.info("Employee records search validation passed")

    def test_loading_of_candidate_records_page(self,logger, maintenance_page):
        # Test: Verify candidate records page loads successfully
        logger = get_logger("test_loading_of_candidate_records_page")
        maintenance = MaintenancePage(maintenance_page)
        logger.info("Opening candidate records page")
        maintenance.open_candidate_records()
        logger.info("Verifying candidate records page heading is visible")
        expect(maintenance.landing_candidate_page_heading).to_be_visible()
        logger.info("Candidate records page loaded successfully")

    def test_search_candidate_records(self,logger, maintenance_page):
        # Test: Search candidate records and verify records exist
        logger = get_logger("test_search_candidate_records")
        maintenance = MaintenancePage(maintenance_page)
        logger.info("Searching for candidate records")
        maintenance.search_candidate_records()
        logger.info("Verifying vacancy cards are present")
        expect(maintenance.vacancy_card).not_to_have_count(0)
        logger.info("Candidate records search passed")

    def test_purge_all_candidate_record(self,logger, maintenance_page):
        # Test: Purge all candidate records and verify deletion
        logger = get_logger("test_purge_all_candidate_record")
        maintenance = MaintenancePage(maintenance_page)
        logger.info("Searching for candidate records to purge")
        maintenance.search_candidate_records()
        logger.info("Purging candidate records")
        maintenance.purge_record()
        logger.info("Verifying all vacancy cards are removed")
        expect(maintenance.vacancy_card).to_have_count(0)
        logger.info("Candidate records purge validation passed")


