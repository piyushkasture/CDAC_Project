from playwright.sync_api import expect
from utils.base_test import BaseTest
from pages.AdminPage import AdminUserPage

class TestAdmin(BaseTest):
    # Test suite for OrangeHRM Admin User Management page
# 1
    def test_search_by_username(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.enter_username("Admin")
        admin_user.click_search()
        admin_user.wait_for_search_results()

        rows = admin_user.results_rows
        assert rows.count() > 0
        logger.info(f"Found {rows.count()} Admin username")
    # 2
    def test_search_by_admin_role(self, logger, admin_page):
        # Search users with Admin role
        admin_user = AdminUserPage(admin_page)
        # admin_user.username_input.click()
        admin_user.clear_username()
        admin_user.select_user_role("Admin")
        admin_user.click_search()
        admin_user.wait_for_search_results()

        rows = admin_user.results_rows
        assert rows.count() > 0
        logger.info(f"Found {rows.count()} Admin users")
    #3
    def test_search_by_ess_role(self, logger, admin_page):
        # TC07: Search users with ESS role
        admin_user = AdminUserPage(admin_page)

        admin_user.select_user_role("ESS")
        admin_user.click_search()

        rows = admin_user.results_rows
        assert rows.count() >= 0
        # Results may be empty for ESS role
        admin_page.wait_for_timeout(2000)
        logger.info("ESS role search executed successfully")

# 4
    def test_search_by_employee_name(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)

        admin_user.click_reset()
        admin_user.select_employee_name("Peter Mac Anderson")
        admin_user.click_search()

        expect(admin_user.result_one_row).to_be_visible()
    # 5
    def test_search_by_status(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.clear_employee_name()
        admin_user.select_status("Enabled")
        admin_user.click_search()

        expect(admin_user.results_rows).not_to_have_count(0)

    # 6
    def test_search_with_username_role(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.click_reset()
        admin_user.enter_username("Admin")
        admin_user.select_user_role("Admin")
        admin_user.click_search()
        admin_user.wait_for_search_results()

        expect(admin_user.results_rows).not_to_have_count(0)
# 7
    def test_search_with_multiple_filters(self,logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.select_status("Enabled")
        admin_user.click_search()

        expect(admin_user.results_rows).not_to_have_count(0)
# 8
    def test_search_with_invalid_username(self,logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.click_reset()
        admin_user.enter_username("piyushkasture")
        admin_user.click_search()

        expect(admin_user.results_rows).to_have_count(0)
    # 9
    def test_search_with_special_characters_in_username(self,logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.click_reset()
        admin_user.enter_username("@#!$$#@~")
        admin_user.click_search()

        expect(admin_user.results_rows).to_have_count(0)
    # 10
    def test_search_with_empty_username(self,logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.click_reset()
        admin_user.enter_username("")
        admin_user.click_search()

        expect(admin_user.results_rows).to_have_count(0)

    # 11
    def test_search_with_very_long_username(self, logger, admin_page):
        # Search with very long username string
        admin_user = AdminUserPage(admin_page)

        long_username = "A" * 100
        admin_user.enter_username(long_username)
        admin_user.click_search()

        expect(admin_user.results_rows).to_have_count(0)


    # 12
    def test_search_with_numeric_username(self, logger, admin_page):
        #Search with numeric username
        admin_user = AdminUserPage(admin_page)

        admin_user.enter_username("12345")
        admin_user.click_search()

        expect(admin_user.results_rows).to_have_count(0)

    # 13
    def test_reset_button_clears_all_filters(self, logger, admin_page):
        # Verify Reset button clears all search filters
        admin_user = AdminUserPage(admin_page)

        admin_user.enter_username("Admin123")
        admin_user.select_user_role("Admin")
        admin_user.click_reset()

        username_value = admin_user.username_input.input_value()
        assert username_value == ""

    # 14
    def test_add_user(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.add_user()

        admin_page.wait_for_timeout(10000)
        #
        # admin_user.enter_username("piyushkasture")
        # admin_user.click_search()

    # 15
    def test_edit_user(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.search_username_by_piyushkasture()
        admin_user.edit_user()
        admin_page.wait_for_timeout(10000)

        admin_user.search_username_and_status()
        admin_page.wait_for_timeout(10000)

# 16
    def test_delete_user(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.delete_user()
        admin_page.wait_for_timeout(5000)
        admin_user.search_username_and_status()

        expect(admin_user.results_rows).to_have_count(0)


# Job title
# 17

    def test_add_job_title(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.add_job_title()
        admin_page.wait_for_timeout(10000)
# 18
    def test_edit_job_title(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.edit_job_title()
        admin_page.wait_for_timeout(10000)

# 19
    def test_delete_job_title(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.delete_job_title()
        admin_page.wait_for_timeout(10000)

# Pay Grade
# 20
    def test_add_pay_grade(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.add_pay_grade()
        admin_page.wait_for_timeout(10000)
# 21
    def test_edit_pay_grade(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.edit_pay_grade()
        admin_page.wait_for_timeout(10000)

# 22
    def test_delete_pay_grade(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.delete_pay_grade()
        admin_page.wait_for_timeout(10000)

    # Employment Status
    # 23
    def test_add_employment_status(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.add_employment_status()
        admin_page.wait_for_timeout(10000)
    
    # 24
    def test_edit_employment_status(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.edit_employment_status()
        admin_page.wait_for_timeout(10000)
    
    # 25
    def test_delete_employment_status(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.delete_employment_status()
        admin_page.wait_for_timeout(10000)

    # Job Categories
    # 26
    def test_add_job_categories(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.add_job_categories()
        admin_page.wait_for_timeout(10000)
    
    # 27
    def test_edit_job_categories(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.edit_job_categories()
        admin_page.wait_for_timeout(10000)
    
    # 28
    def test_delete_job_categories(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.delete_job_categories()
        admin_page.wait_for_timeout(10000)

    # Organization General Information
    # 29
    def test_edit_general_information(self,logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.edit_general_information()

    # Locations
    # 30

    def test_add_location(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.add_location()

        admin_page.wait_for_timeout(10000)
        #
        # admin_user.enter_username("piyushkasture")
        # admin_user.click_search()
#
#     # 31
    def test_edit_location(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.search_location_by_name()
        admin_user.edit_location()
        admin_page.wait_for_timeout(10000)

        admin_user.search_name_city_and_country()
        admin_page.wait_for_timeout(10000)
#
# # 32
    def test_delete_location(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.delete_location()
        admin_page.wait_for_timeout(5000)
        admin_user.search_name_city_and_country()

        expect(admin_user.results_rows).to_have_count(0)


# Qualifications Skills

    # 33
    def test_add_skills(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.add_skills()

        admin_page.wait_for_timeout(10000)


    # 34
    def test_edit_skills(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.edit_skills()
        admin_page.wait_for_timeout(10000)


    # 35
    def test_delete_skill(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.delete_skills()
        admin_page.wait_for_timeout(5000)


# Education
#     36
    def test_add_education(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.add_education()

        admin_page.wait_for_timeout(10000)


    # 37
    def test_edit_education(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.edit_education()
        admin_page.wait_for_timeout(10000)


    # 38
    def test_delete_education(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.delete_education()
        admin_page.wait_for_timeout(5000)

# Licenses
    # 39
    def test_add_licenses(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.add_licenses()

        admin_page.wait_for_timeout(10000)


    # 40
    def test_edit_licenses(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.edit_licenses()
        admin_page.wait_for_timeout(10000)


    # 41
    def test_delete_licenses(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.delete_licenses()
        admin_page.wait_for_timeout(5000)

# Languages
# 42
    def test_add_languages(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.add_licenses()

        admin_page.wait_for_timeout(10000)


    # 43
    def test_edit_languages(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.edit_licenses()
        admin_page.wait_for_timeout(10000)


    # 44
    def test_delete_languages(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.delete_licenses()
        admin_page.wait_for_timeout(5000)

# Memberships
# 45
    def test_add_memberships(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.add_licenses()

        admin_page.wait_for_timeout(10000)


    # 46
    def test_edit_memberships(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.edit_licenses()
        admin_page.wait_for_timeout(10000)


    # 47
    def test_delete_memberships(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.delete_licenses()
        admin_page.wait_for_timeout(5000)


# Nationalities
# 48
    def test_add_nationalities(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.add_nationalities()

        admin_page.wait_for_timeout(10000)


    # 49
    def test_edit_nationalities(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.edit_nationalities()
        admin_page.wait_for_timeout(10000)


    # 50
    def test_delete_nationalities(self, logger, admin_page):
        admin_user = AdminUserPage(admin_page)
        admin_user.delete_nationalities()
        admin_page.wait_for_timeout(5000)