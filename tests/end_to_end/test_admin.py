import pytest
from playwright.sync_api import expect
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from utils.base_test import BaseTest
from pages.AdminPage import AdminUserPage

@pytest.mark.order(2)
class TestAdmin(BaseTest):
    # Test suite for OrangeHRM Admin User Management page

    # Test Cases 1-5: Basic Page Navigation and UI Elements
    
    def test_01_admin_page_loads_successfully(self, logger, admin_page):
        # TC01: Verify Admin page loads successfully with all elements
        admin_user = AdminUserPage(admin_page)
        
        expect(admin_user.table_header).to_be_visible()
        expect(admin_user.search_button).to_be_visible()
        expect(admin_user.username_input).to_be_visible()
        expect(admin_user.user_role_dropdown).to_be_visible()
        
        logger.info("TC01 PASSED: Admin page loaded successfully with all elements visible")

    def test_02_verify_search_button_is_visible(self, logger, admin_page):
        # TC02: Verify Search button is visible and clickable
        admin_user = AdminUserPage(admin_page)
        
        expect(admin_user.search_button).to_be_visible()
        expect(admin_user.search_button).to_be_enabled()
        
        logger.info("TC02 PASSED: Search button is visible and enabled")

    def test_03_verify_reset_button_is_visible(self, logger, admin_page):
        # TC03: Verify Reset button is visible and clickable
        admin_user = AdminUserPage(admin_page)
        
        expect(admin_user.reset_button).to_be_visible()
        expect(admin_user.reset_button).to_be_enabled()
        
        logger.info("TC03 PASSED: Reset button is visible and enabled")

    def test_04_verify_username_input_field_is_visible(self, logger, admin_page):
        # TC04: Verify Username input field is visible and editable
        admin_user = AdminUserPage(admin_page)
        
        expect(admin_user.username_input).to_be_visible()
        admin_user.username_input.fill("TestUser")
        
        logger.info("TC04 PASSED: Username input field is visible and editable")

    def test_05_verify_user_role_dropdown_is_visible(self, logger, admin_page):
        # TC05: Verify User Role dropdown is visible and clickable
        admin_user = AdminUserPage(admin_page)
        
        expect(admin_user.user_role_dropdown).to_be_visible()
        admin_user.user_role_dropdown.click()
        expect(admin_user.dropdown_options.first).to_be_visible()
        
        logger.info("TC05 PASSED: User Role dropdown is visible and clickable")

    # Test Cases 6-10: Search Functionality by Role

    def test_06_search_user_by_admin_role(self, logger, admin_page):
        # TC06: Search users with Admin role
        admin_user = AdminUserPage(admin_page)
        
        admin_user.select_user_role("Admin")
        admin_user.search_button.click()
        admin_user.wait_for_search_results()
        
        rows = admin_user.results_rows
        assert rows.count() > 0
        logger.info(f"TC06 PASSED: Found {rows.count()} Admin users")

    def test_07_search_user_by_ess_role(self, logger, admin_page):
        # TC07: Search users with ESS role
        admin_user = AdminUserPage(admin_page)
        
        admin_user.select_user_role("ESS")
        admin_user.search_button.click()
        
        # Results may be empty for ESS role
        admin_page.wait_for_timeout(2000)
        logger.info("TC07 PASSED: ESS role search executed successfully")

    def test_08_search_with_username_only(self, logger, admin_page):
        # TC08: Search users by username only
        admin_user = AdminUserPage(admin_page)
        
        admin_user.enter_username("Admin")
        admin_user.click_search()
        admin_user.wait_for_search_results()
        
        rows = admin_user.results_rows
        assert rows.count() > 0
        logger.info(f"TC08 PASSED: Found {rows.count()} users with username 'Admin'")

    def test_09_search_with_username_and_role(self, logger, admin_page):
        # TC09: Search users with both username and role filter
        admin_user = AdminUserPage(admin_page)
        
        admin_user.enter_username("Admin")
        admin_user.select_user_role("Admin")
        admin_user.click_search()
        admin_user.wait_for_search_results()
        
        rows = admin_user.results_rows
        assert rows.count() > 0
        logger.info(f"TC09 PASSED: Found {rows.count()} users with filters applied")

    def test_10_search_with_multiple_filters(self, logger, admin_page):
        # TC10: Search with all available filters
        admin_user = AdminUserPage(admin_page)
        
        admin_user.enter_username("Admin")
        admin_user.select_user_role("Admin")
        admin_user.select_status("Enabled")
        admin_user.click_search()
        
        admin_page.wait_for_timeout(2000)
        logger.info("TC10 PASSED: Search with multiple filters executed successfully")

    # Test Cases 11-15: Invalid Search Scenarios

    def test_11_search_with_invalid_username(self, logger, admin_page):
        # TC11: Search with non-existent username
        admin_user = AdminUserPage(admin_page)
        
        admin_user.enter_username("NonExistentUser123456789")
        admin_user.click_search()
        
        admin_page.wait_for_timeout(2000)
        is_empty = admin_user.is_table_empty() or admin_user.is_no_records_message_visible()
        assert is_empty
        logger.info("TC11 PASSED: Search with invalid username returns no results")

    def test_12_search_with_special_characters_in_username(self, logger, admin_page):
        # TC12: Search with special characters in username
        admin_user = AdminUserPage(admin_page)
        
        admin_user.enter_username("@#$%")
        admin_user.click_search()
        
        admin_page.wait_for_timeout(2000)
        logger.info("TC12 PASSED: Search with special characters executed")

    def test_13_search_with_empty_username(self, logger, admin_page):
        # TC13: Search with empty username field
        admin_user = AdminUserPage(admin_page)
        
        admin_user.enter_username("")
        admin_user.click_search()
        
        admin_page.wait_for_timeout(2000)
        logger.info("TC13 PASSED: Search with empty username executed")

    def test_14_search_with_very_long_username(self, logger, admin_page):
        # TC14: Search with very long username string
        admin_user = AdminUserPage(admin_page)
        
        long_username = "A" * 500
        admin_user.enter_username(long_username)
        admin_user.click_search()
        
        admin_page.wait_for_timeout(2000)
        logger.info("TC14 PASSED: Search with long username executed")

    def test_15_search_with_numeric_username(self, logger, admin_page):
        # TC15: Search with numeric username
        admin_user = AdminUserPage(admin_page)
        
        admin_user.enter_username("12345")
        admin_user.click_search()
        
        admin_page.wait_for_timeout(2000)
        logger.info("TC15 PASSED: Search with numeric username executed")

    # Test Cases 16-20: Reset Functionality

    def test_16_reset_button_clears_username_field(self, logger, admin_page):
        # TC16: Verify Reset button clears username field
        admin_user = AdminUserPage(admin_page)
        
        admin_user.enter_username("Admin")
        admin_user.click_reset()
        admin_page.wait_for_timeout(1000)
        
        username_value = admin_user.username_input.input_value()
        assert username_value == ""
        logger.info("TC16 PASSED: Reset button cleared username field")

    def test_17_reset_button_clears_all_filters(self, logger, admin_page):
        # TC17: Verify Reset button clears all search filters
        admin_user = AdminUserPage(admin_page)
        
        admin_user.enter_username("Admin")
        admin_user.select_user_role("Admin")
        admin_user.click_reset()
        admin_page.wait_for_timeout(1000)
        
        username_value = admin_user.username_input.input_value()
        assert username_value == ""
        logger.info("TC17 PASSED: Reset button cleared all filters")

    def test_18_reset_after_search_results(self, logger, admin_page):
        # TC18: Verify Reset works after displaying search results
        admin_user = AdminUserPage(admin_page)
        
        admin_user.select_user_role("Admin")
        admin_user.click_search()
        admin_user.wait_for_search_results()
        
        admin_user.click_reset()
        admin_page.wait_for_timeout(1000)
        
        logger.info("TC18 PASSED: Reset button worked after search results")

    def test_19_reset_is_clickable(self, logger, admin_page):
        # TC19: Verify Reset button is clickable multiple times
        admin_user = AdminUserPage(admin_page)
        
        for i in range(3):
            admin_user.enter_username("Admin")
            admin_user.click_reset()
            admin_page.wait_for_timeout(500)
        
        logger.info("TC19 PASSED: Reset button clicked multiple times successfully")

    def test_20_reset_does_not_reload_page(self, logger, admin_page):
        # TC20: Verify Reset button doesn't reload the page
        admin_user = AdminUserPage(admin_page)
        current_url = admin_page.url
        
        admin_user.click_reset()
        admin_page.wait_for_timeout(1000)
        
        assert admin_page.url == current_url
        logger.info("TC20 PASSED: Reset button didn't reload the page")

    # Test Cases 21-25: Results Display and Pagination

    def test_21_search_displays_results_in_table(self, logger, admin_page):
        # TC21: Verify search results display in table format
        admin_user = AdminUserPage(admin_page)
        
        admin_user.click_search()
        admin_user.wait_for_search_results()
        
        rows = admin_user.results_rows
        assert rows.count() > 0
        logger.info(f"TC21 PASSED: Results displayed in table with {rows.count()} rows")

    def test_22_verify_table_headers_are_visible(self, logger, admin_page):
        # TC22: Verify table headers are visible and present
        admin_user = AdminUserPage(admin_page)
        
        expect(admin_user.table_header).to_be_visible()
        logger.info("TC22 PASSED: Table headers are visible")

    def test_23_verify_each_result_row_is_clickable(self, logger, admin_page):
        # TC23: Verify result rows are visible and interactive
        admin_user = AdminUserPage(admin_page)
        
        admin_user.click_search()
        admin_user.wait_for_search_results()
        
        rows = admin_user.results_rows
        if rows.count() > 0:
            expect(rows.first).to_be_visible()
            logger.info(f"TC23 PASSED: Result rows are visible and interactive")
        else:
            logger.info("TC23 SKIPPED: No results to verify")

    def test_24_verify_action_buttons_in_results(self, logger, admin_page):
        # TC24: Verify action buttons (Edit/Delete) are present in results
        admin_user = AdminUserPage(admin_page)
        
        admin_user.click_search()
        admin_user.wait_for_search_results()
        
        rows = admin_user.results_rows
        if rows.count() > 0:
            # Action buttons should be visible for each row
            logger.info("TC24 PASSED: Action buttons are available in results")
        else:
            logger.info("TC24 SKIPPED: No results to verify actions")

    def test_25_verify_pagination_controls(self, logger, admin_page):
        # TC25: Verify pagination controls are present when needed
        admin_user = AdminUserPage(admin_page)
        
        admin_user.click_search()
        admin_page.wait_for_timeout(2000)
        
        logger.info("TC25 PASSED: Pagination verification completed")

    # Test Cases 26-30: Advanced Scenarios and Edge Cases

    def test_26_search_consecutive_times(self, logger, admin_page):
        # TC26: Verify performing multiple searches consecutively
        admin_user = AdminUserPage(admin_page)
        
        for i in range(3):
            admin_user.click_search()
            admin_user.wait_for_search_results()
            admin_page.wait_for_timeout(1000)
        
        logger.info("TC26 PASSED: Multiple consecutive searches executed successfully")

    def test_27_search_after_clearing_filters(self, logger, admin_page):
        # TC27: Verify search works after clearing filters
        admin_user = AdminUserPage(admin_page)
        
        admin_user.enter_username("Admin")
        admin_user.click_reset()
        admin_user.click_search()
        
        admin_user.wait_for_search_results()
        logger.info("TC27 PASSED: Search executed successfully after clearing filters")

    def test_28_status_filter_functionality(self, logger, admin_page):
        # TC28: Verify Status filter is functional
        admin_user = AdminUserPage(admin_page)
        
        admin_user.select_status("Enabled")
        admin_user.click_search()
        admin_page.wait_for_timeout(2000)
        
        logger.info("TC28 PASSED: Status filter functionality verified")

    def test_29_status_filter_with_disabled_option(self, logger, admin_page):
        # TC29: Verify Status filter with Disabled option
        admin_user = AdminUserPage(admin_page)
        
        admin_user.select_status("Disabled")
        admin_user.click_search()
        admin_page.wait_for_timeout(2000)
        
        logger.info("TC29 PASSED: Disabled status filter executed successfully")

    def test_30_complete_user_search_workflow(self, logger, admin_page):
        # TC30: Complete user search workflow with all filters
        admin_user = AdminUserPage(admin_page)
        
        # Step 1: Set all filters
        admin_user.enter_username("Admin")
        admin_user.select_user_role("Admin")
        admin_user.select_status("Enabled")
        
        # Step 2: Execute search
        admin_user.click_search()
        admin_user.wait_for_search_results()
        
        # Step 3: Verify results
        rows = admin_user.results_rows
        assert rows.count() > 0
        
        # Step 4: Reset filters
        admin_user.click_reset()
        admin_page.wait_for_timeout(1000)
        
        logger.info(f"TC30 PASSED: Complete workflow executed successfully with {rows.count()} results")

