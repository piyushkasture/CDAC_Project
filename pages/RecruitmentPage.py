from pages.BasePage import BasePage


class RecruitmentPage(BasePage):

    RECRUITMENT_HEADER = "//h6[text()='Recruitment']"
    CANDIDATE_NAME = "//input[@placeholder='Type for hints...']"
    SEARCH_BUTTON = "//button[@type='submit']"
    RECORD_FOUND = "(//div[@role='row'])[2]"

    def is_recruitment_page_loaded(self):
        self.wait_for_element(self.RECRUITMENT_HEADER)
        return self.is_visible(self.RECRUITMENT_HEADER)

    def search_candidate(self, name):
        self.fill(self.CANDIDATE_NAME, name)
        self.click(self.SEARCH_BUTTON)

    def record_found(self):
        self.wait_for_element(self.RECORD_FOUND)
        return self.is_visible(self.RECORD_FOUND)

