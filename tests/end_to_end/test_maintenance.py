import pytest
from playwright.sync_api import Page, expect
from pages.MaintenancePage import MaintenancePage


# @pytest.mark.usefixtures("login_as_admin")
class TestMaintenance:

    def test_to_test_access_to_maintenance_module(self, page: Page):
        maintenance = MaintenancePage(page)
        maintenance.open_maintenance("admin123")

        expect(page).to_have_url(lambda url: "maintenance" in url)


    def test_to_test_loading_of_employee_records_page(self, page: Page):
        maintenance = MaintenancePage(page)
        maintenance.open_maintenance("admin123")
        maintenance.open_employee_records()

        expect(page.locator("text=Purge Employee Records")).to_be_visible()


    def test_to_test_search_employee_records(self, page: Page):
        maintenance = MaintenancePage(page)
        maintenance.open_maintenance("admin123")
        maintenance.open_employee_records()

        maintenance.search_record("Paul")

        expect(page.locator(".oxd-table-body")).to_be_visible()


    def test_to_test_purge_single_employee_record(self, page: Page):
        maintenance = MaintenancePage(page)
        maintenance.open_maintenance("admin123")
        maintenance.open_employee_records()

        maintenance.search_record("Paul")
        maintenance.purge_record()

        expect(page.locator("text=Successfully Purged")).to_be_visible()


    def test_to_test_cancel_employee_purge_action(self, page: Page):
        maintenance = MaintenancePage(page)
        maintenance.open_maintenance("admin123")
        maintenance.open_employee_records()

        maintenance.search_record("Paul")
        maintenance.cancel_purge()

        expect(page.locator("text=Purge Employee Records")).to_be_visible()


    def test_to_test_loading_of_candidate_records_page(self, page: Page):
        maintenance = MaintenancePage(page)
        maintenance.open_maintenance("admin123")
        maintenance.open_candidate_records()

        expect(page.locator("text=Purge Candidate Records")).to_be_visible()


    def test_to_test_search_candidate_records(self, page: Page):
        maintenance = MaintenancePage(page)
        maintenance.open_maintenance("admin123")
        maintenance.open_candidate_records()

        maintenance.search_record("John")

        expect(page.locator(".oxd-table-body")).to_be_visible()


    def test_to_test_purge_single_candidate_record(self, page: Page):
        maintenance = MaintenancePage(page)
        maintenance.open_maintenance("admin123")
        maintenance.open_candidate_records()

        maintenance.search_record("John")
        maintenance.purge_record()

        expect(page.locator("text=Successfully Purged")).to_be_visible()


    def test_to_test_navigation_between_employee_and_candidate_pages(self, page: Page):
        maintenance = MaintenancePage(page)
        maintenance.open_maintenance("admin123")

        maintenance.open_employee_records()
        expect(page.locator("text=Purge Employee Records")).to_be_visible()

        maintenance.open_candidate_records()
        expect(page.locator("text=Purge Candidate Records")).to_be_visible()


    def test_to_test_multiple_purge_operations_in_single_session(self, page: Page):
        maintenance = MaintenancePage(page)
        maintenance.open_maintenance("admin123")

        maintenance.open_employee_records()
        maintenance.search_record("Paul")
        maintenance.purge_record()

        maintenance.open_candidate_records()
        maintenance.search_record("John")
        maintenance.purge_record()

        expect(page).to_have_url(lambda url: "maintenance" in url)

    def test_to_test_maintenance_access_with_invalid_password(self, page: Page):
        maintenance = MaintenancePage(page)
        maintenance.open_maintenance_with_invalid_password("wrongpass")

        expect(maintenance.error_message).to_be_visible()

    def test_to_test_maintenance_access_with_blank_password(self, page: Page):
        maintenance = MaintenancePage(page)
        maintenance.open_maintenance_with_invalid_password("")

        expect(maintenance.error_message).to_be_visible()

    def test_to_test_search_employee_with_invalid_name(self, page: Page):
        maintenance = MaintenancePage(page)
        maintenance.open_maintenance("admin123")
        maintenance.open_employee_records()

        maintenance.search_with_invalid_name("InvalidEmployee123")

        expect(maintenance.no_records_found).to_be_visible()

    def test_to_test_search_candidate_with_invalid_name(self, page: Page):
        maintenance = MaintenancePage(page)
        maintenance.open_maintenance("admin123")
        maintenance.open_candidate_records()

        maintenance.search_with_invalid_name("InvalidCandidate123")

        expect(maintenance.no_records_found).to_be_visible()

    def test_to_test_purge_without_selecting_employee_record(self, page: Page):
        maintenance = MaintenancePage(page)
        maintenance.open_maintenance("admin123")
        maintenance.open_employee_records()

        maintenance.attempt_purge_without_selection()

        expect(maintenance.error_message).to_be_visible()

    def test_to_test_cancel_purge_action_for_employee_record(self, page: Page):
        maintenance = MaintenancePage(page)
        maintenance.open_maintenance("admin123")
        maintenance.open_employee_records()

        maintenance.search_record("Paul")
        maintenance.cancel_purge()

        expect(page.locator("text=Purge Employee Records")).to_be_visible()

    def test_to_test_cancel_purge_action_for_candidate_record(self, page: Page):
        maintenance = MaintenancePage(page)
        maintenance.open_maintenance("admin123")
        maintenance.open_candidate_records()

        maintenance.search_record("John")
        maintenance.cancel_purge()

        expect(page.locator("text=Purge Candidate Records")).to_be_visible()

    def test_to_test_purge_already_deleted_employee_record(self, page: Page):
        maintenance = MaintenancePage(page)
        maintenance.open_maintenance("admin123")
        maintenance.open_employee_records()

        maintenance.search_record("DeletedEmployee")

        expect(maintenance.no_records_found).to_be_visible()

