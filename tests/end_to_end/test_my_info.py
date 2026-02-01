# import pytest
from playwright.sync_api import expect
from pages.MyInfoPage import MyInfoPage


# @pytest.mark.myinfo
# class TestMyInfoFullSuite:

    # # ---------- NAVIGATION (1–5) ----------
    # def test_01_open_my_info(self, page):
    #     mi = MyInfoPage(page)
    #     mi.open_my_info()
    #     expect(page).to_have_url_containing("viewMyDetails")

    # def test_02_refresh_page(self, page):
    #     page.reload()
    #     expect(page.get_by_text("Personal Details")).to_be_visible()
    #
    # def test_03_employee_id_readonly(self, page):
    #     expect(page.locator("input[name='employeeId']")).to_be_disabled()
    #
    # def test_04_gender_radio(self, page):
    #     expect(page.get_by_label("Male")).to_be_visible()
    #
    # def test_05_dob_picker(self, page):
    #     page.get_by_placeholder("Date of Birth").click()
    #     expect(page.locator(".oxd-date-input-calendar")).to_be_visible()

    # ---------- PERSONAL POSITIVE (6–9) ----------
    # @pytest.mark.parametrize("d", my_info_data_read["personal_positive"])
def test_06_update_personal_positive(page, myinfo_page, get_my_info_data):
    mi = MyInfoPage(myinfo_page)
    mi.update_personal(get_my_info_data["personal_positive"]["data1"]["first"], get_my_info_data["personal_positive"]["data1"]["last"], get_my_info_data["personal_positive"]["data1"]["nick"])
    expect(page.get_by_text("Successfully Updated")).to_be_visible()

def test_07_update_personal_positive(page, myinfo_page, get_my_info_data):
    mi = MyInfoPage(myinfo_page)
    mi.update_personal(get_my_info_data["personal_positive"]["data2"]["first"],
                           get_my_info_data["personal_positive"]["data2"]["last"],
                           get_my_info_data["personal_positive"]["data2"]["nick"])
    expect(page.get_by_text("Successfully Updated")).to_be_visible()


    # ---------- PERSONAL NEGATIVE (10–12) ----------
    # @pytest.mark.parametrize("d", my_info_data_read["personal_negative"])
    # def test_10_update_personal_negative(self, page):
    #     mi = MyInfoPage(page)
    #     mi.update_personal(my_info_data_read["personal_negative"]["first"], my_info_data_read["personal_negative"]["last"])
    #     expect(page.get_by_text("Required")).to_be_visible()

    # ---------- CONTACT POSITIVE (13–15) ----------
    # @pytest.mark.parametrize("d", my_info_data_read["contact_positive"])
    # def test_13_contact_positive(self, page):
    #     mi = MyInfoPage(page)
    #     mi.open_tab("Contact Details")
    #     mi.update_contact(my_info_data_read["contact_positive"]["mobile"], my_info_data_read["contact_positive"]["email"], my_info_data_read["contact_positive"]["address"])
    #     expect(page.get_by_text("Successfully Updated")).to_be_visible()

    # # ---------- CONTACT NEGATIVE (16–18) ----------
    # @pytest.mark.parametrize("d", my_info_data_read["contact_negative"])
    # def test_16_contact_negative(self, page, d):
    #     mi = MyInfoPage(page)
    #     mi.open_tab("Contact Details")
    #     mi.update_contact(d["mobile"], d["email"])
    #     expect(page.get_by_text("Invalid")).to_be_visible()
    #
    # # ---------- EMERGENCY POSITIVE (19–21) ----------
    # @pytest.mark.parametrize("d", my_info_data_read["emergency_positive"])
    # def test_19_emergency_positive(self, page, d):
    #     mi = MyInfoPage(page)
    #     mi.open_tab("Emergency Contacts")
    #     mi.add_emergency(d["name"], d["relation"], d["mobile"])
    #     expect(page.get_by_text("Successfully Saved")).to_be_visible()
    #
    # # ---------- EMERGENCY NEGATIVE (22–23) ----------
    # @pytest.mark.parametrize("d", my_info_data_read["emergency_negative"])
    # def test_22_emergency_negative(self, page, d):
    #     mi = MyInfoPage(page)
    #     mi.open_tab("Emergency Contacts")
    #     mi.add_emergency(d["name"], d["relation"], d["mobile"])
    #     expect(page.get_by_text("Required")).to_be_visible()
    #
    # # ---------- DEPENDENTS POSITIVE (24–26) ----------
    # @pytest.mark.parametrize("d", data["dependents_positive"])
    # def test_24_dependent_positive(self, page, d):
    #     mi = MyInfoPage(page)
    #     mi.open_tab("Dependents")
    #     mi.add_dependent(d["name"], d["dob"])
    #     expect(page.get_by_text("Successfully Saved")).to_be_visible()
    #
    # # ---------- DEPENDENTS NEGATIVE (27–28) ----------
    # @pytest.mark.parametrize("d", data["dependents_negative"])
    # def test_27_dependent_negative(self, page, d):
    #     mi = MyInfoPage(page)
    #     mi.open_tab("Dependents")
    #     mi.add_dependent(d["name"], d["dob"])
    #     expect(page.get_by_text("Required")).to_be_visible()
    #
    # # ---------- ATTACHMENT POSITIVE (29–31) ----------
    # @pytest.mark.parametrize("d", data["attachments_positive"])
    # def test_29_attachment_positive(self, page, d):
    #     mi = MyInfoPage(page)
    #     mi.open_my_info()
    #     mi.upload_attachment(d["file"], d["comment"])
    #     expect(page.get_by_text("Successfully Uploaded")).to_be_visible()
    #
    # # ---------- ATTACHMENT NEGATIVE (32–34) ----------
    # @pytest.mark.parametrize("d", data["attachments_negative"])
    # def test_32_attachment_negative(self, page, d):
    #     mi = MyInfoPage(page)
    #     mi.upload_attachment(d["file"], d["comment"])
    #     expect(page.get_by_text("File type not allowed")).to_be_visible()
    #
    # # ---------- FINAL SANITY (35–36) ----------
    # def test_35_logout_not_allowed_here(self, page):
    #     expect(page.locator("header")).to_be_visible()
    #
    # def test_36_session_alive(self, page):
    #     expect(page.get_by_text("My Info")).to_be_visible()
