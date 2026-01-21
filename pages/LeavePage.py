from pages.BasePage import BasePage


class LeavePage(BasePage):

    LEAVE_HEADER = "//h6[text()='Leave']"
    FROM_DATE = "(//input[@placeholder='yyyy-dd-mm'])[1]"
    TO_DATE = "(//input[@placeholder='yyyy-dd-mm'])[2]"
    SEARCH_BUTTON = "//button[@type='submit']"
    No_Record_Found = "//span[text()='No Records Found']"

    def is_leave_page_loaded(self):
        self.wait_for_element(self.LEAVE_HEADER)
        return self.is_visible(self.LEAVE_HEADER)

    def search_leave(self, from_date, to_date):
        self.fill(self.FROM_DATE, from_date)
        self.fill(self.TO_DATE, to_date)
        self.click(self.SEARCH_BUTTON)

    def no_record_found(self):
        return self.get_text(self.No_Record_Found)