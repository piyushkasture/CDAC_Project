from logging import Logger
from playwright.sync_api import Page, expect
from pages.BasePage import BasePage


class AdminUserPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # self.page = page
        self.username_input = page.locator("(//input[@class='oxd-input oxd-input--active'])[2]")
        self.user_role_dropdown = page.locator("//label[text()='User Role']/following::div[contains(@class,'oxd-select-text')][1]")
        self.employee_name_input = page.locator("(//input[@placeholder='Type for hints...'])[1]")
        self.status_dropdown = page.locator("//label[text()='Status']/following::div[contains(@class,'oxd-select-text')][1]")
        self.dropdown_options = page.locator("//div[@role='listbox']//span")
        self.search_button = page.locator("//button[@type='submit']")
        self.reset_button = page.locator("//button[normalize-space()='Reset']")
        self.add_button = page.locator("//button[contains(text(), 'Add')]")
        self.results_rows = page.locator("div.oxd-table-body div.oxd-table-card")
        self.no_records = page.locator("span:has-text('No Records Found')")
        self.table_header = page.locator("div.oxd-table-header")
        self.pagination = page.locator("//ul[@class='oxd-pagination__list']")
        self.edit_buttons = page.locator("//i[@class='oxd-icon bi-pencil-fill']")
        self.delete_buttons = page.locator("//i[@class='oxd-icon bi-trash']")
        self.confirm_delete_button = page.locator("//button[contains(text(), 'Yes, Delete')]")
        self.cancel_button = page.locator("//button[normalize-space()='Cancel']")
        self.modal_title = page.locator("//h6[@class='oxd-text oxd-text--h6']")
        self.success_message = page.locator("//div[@class='oxd-toast-content']")
        self.save_button = page.locator("//button[@type='submit'][contains(text(), 'Save')]")
        self.username_field = page.locator("//label[text()='Username']/following::input[1]")

    def wait_for_search_results(self):
        expect(self.results_rows.first).to_be_visible(timeout=10000)
        
    def wait_for_no_results(self):
        try:
            expect(self.no_records).to_be_visible(timeout=5000)
            return True
        except:
            return False

    def select_user_role(self, role_name):
        # Click on User Role dropdown
        self.user_role_dropdown.click()
        # Select required role (Admin / ESS)
        self.dropdown_options.filter(has_text=role_name).first.click()

    def select_status(self, status_value):
        # Click on Status dropdown
        self.status_dropdown.click()
        # Select required status
        self.dropdown_options.filter(has_text=status_value).first.click()

    def enter_username(self, username):
        self.username_input.fill(username)

    def clear_username(self):
        self.username_input.clear()

    def enter_employee_name(self, employee_name):
        self.employee_name_input.fill(employee_name)

    def clear_employee_name(self):
        self.employee_name_input.clear()

    def click_search(self):
        self.search_button.click()

    def click_reset(self):
        self.reset_button.click()

    def click_add(self):
        self.add_button.click()

    def get_row_count(self):
        return self.results_rows.count()

    def click_edit_button(self, row_index=0):
        self.edit_buttons.nth(row_index).click()

    def click_delete_button(self, row_index=0):
        self.delete_buttons.nth(row_index).click()

    def confirm_delete(self):
        self.confirm_delete_button.click()

    def get_success_message(self):
        expect(self.success_message).to_be_visible(timeout=5000)
        return self.success_message.text_content()

    def is_table_empty(self):
        return self.results_rows.count() == 0

    def is_no_records_message_visible(self):
        try:
            expect(self.no_records).to_be_visible(timeout=3000)
            return True
        except:
            return False


