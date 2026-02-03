from playwright.sync_api import expect
from pages.MyInfoPage import MyInfoPage
from utils.base_test import BaseTest

class TestMyInfo(BaseTest):

    def test_update_personal_details(self, logger, myinfo_page, get_my_info_data):
        # Test: Update Personal Details with name and middle name
        myinfo = MyInfoPage(myinfo_page)
        logger.info("Starting test to update personal details")
        myinfo.update_personal(get_my_info_data)
        myinfo_page.wait_for_timeout(10000)
        logger.info("Personal details updated successfully")

    def test_contact_details_update(self, logger, myinfo_page, get_my_info_data):
        # Test: Update Contact Details with mobile, email, and street address
        myinfo = MyInfoPage(myinfo_page)
        logger.info("Opening Contact Details section")
        myinfo.open_contact_details()
        contact = get_my_info_data["contact"]
        logger.info(f"Updating contact with mobile: {contact['mobile']}, email: {contact['email']}")
        myinfo.update_contact(contact["mobile"], contact["email"], contact.get("street1"))
        myinfo_page.wait_for_timeout(10000)
        logger.info("Contact details updated successfully")

    def test_emergency_contacts_add_edit_delete(self, logger, myinfo_page, get_my_info_data):
        # Test: Add, Edit, and Delete Emergency Contact
        myinfo = MyInfoPage(myinfo_page)
        logger.info("Opening Emergency Contacts section")
        myinfo.open_emergency_contacts()
        ec = get_my_info_data["emergency_contact"]
        logger.info(f"Adding emergency contact: {ec['name']}")
        myinfo.add_emergency_contact(ec["name"], ec["relationship"], ec["home_phone"])
        myinfo_page.wait_for_timeout(10000)
        logger.info("Editing emergency contact")
        myinfo.edit_emergency_contact()
        myinfo_page.wait_for_timeout(5000)
        logger.info("Deleting emergency contact")
        myinfo.delete_emergency_contact()
        myinfo_page.wait_for_timeout(5000)
    
    def test_dependents_add_edit_delete(self, logger, myinfo_page, get_my_info_data):
        # Test: Add, Edit, and Delete Dependent
        myinfo = MyInfoPage(myinfo_page)
        logger.info("Opening Dependents section")
        myinfo.open_dependents()
        dep = get_my_info_data["dependent"]
        logger.info(f"Adding dependent: {dep['name']} with DOB: {dep['dob']}")
        myinfo.add_dependent(dep["name"],dep["dob"])
        myinfo_page.wait_for_timeout(5000)
        logger.info(f"Editing dependent to: {dep['edit_name']}")
        myinfo.edit_dependent(dep["edit_name"])
        myinfo_page.wait_for_timeout(5000)
        logger.info("Deleting dependent")
        myinfo.delete_dependent()
        myinfo_page.wait_for_timeout(5000)
    
    def test_immigration_add_edit_delete(self, logger, myinfo_page, get_my_info_data):
        # Test: Add, Edit, and Delete Immigration Document
        myinfo = MyInfoPage(myinfo_page)
        logger.info("Opening Immigration section")
        myinfo.open_immigration()
        im = get_my_info_data["immigration"]
        logger.info(f"Adding immigration document: {im['number']}")
        myinfo.add_immigration(im["number"], im["issued_date"], im["expiry_date"], im.get("eligible_status", "Yes"))
        myinfo_page.wait_for_timeout(5000)
        logger.info(f"Editing immigration to: {im['edit_number']}")
        myinfo.edit_immigration(im["edit_number"])
        myinfo_page.wait_for_timeout(5000)
        logger.info("Deleting immigration document")
        myinfo.delete_immigration()
        myinfo_page.wait_for_timeout(5000)
    
    def test_job_details(self, logger, myinfo_page):
        # Test: Verify Job section is visible
        myinfo = MyInfoPage(myinfo_page)
        logger.info("Opening Job section")
        myinfo.open_job()
        logger.info("Verifying Job section visibility")
        myinfo.is_job_section_visible()
    
    def test_salary_details(self, logger, myinfo_page):
        # Test: Verify Salary section is visible
        myinfo = MyInfoPage(myinfo_page)
        logger.info("Opening Salary section")
        myinfo.open_salary()
        logger.info("Verifying Salary section visibility")
        myinfo.is_salary_section_visible()
    #
    def test_report_to_details(self, logger, myinfo_page):
        # Test: Verify Report-to section is visible
        myinfo = MyInfoPage(myinfo_page)
        logger.info("Opening Report-to section")
        myinfo.open_report_to()
        logger.info("Verifying Report-to section visibility")
        myinfo.is_report_to_section_visible()
    #
    def test_qualifications_work_experiance(self, logger, myinfo_page, get_my_info_data):
        # Test: Add, Edit, and Delete Work Experience
        myinfo = MyInfoPage(myinfo_page)
        logger.info("Opening Qualifications section")
        myinfo.open_qualifications()
        we = get_my_info_data["work_experience"]
        logger.info(f"Adding work experience at {we['company']} as {we['job_title']}")
        myinfo.add_work_experience(we["company"], we["job_title"], we["from_date"], we["to_date"])
        myinfo_page.wait_for_timeout(5000)
        logger.info(f"Editing work experience: {we['company']}")
        myinfo.edit_work_experiance(we["company"])
        logger.info("Deleting work experience")
        myinfo.delete_reusable_function(we["company"])
        myinfo_page.wait_for_timeout(5000)
    
    def test_qualifications_education(self, logger, myinfo_page, get_my_info_data):
        # Test: Add, Edit, and Delete Education Record
        myinfo = MyInfoPage(myinfo_page)
        edu = get_my_info_data["education"]
        logger.info(f"Adding education from {edu['institute']} for year {edu['year']}")
        myinfo.add_education(edu["institute"], edu["year"])
        myinfo_page.wait_for_timeout(5000)
        logger.info(f"Editing education year to: {edu['year']}")
        myinfo.edit_education(edu["year"])
        myinfo_page.wait_for_timeout(5000)
        logger.info("Deleting education record")
        myinfo.delete_reusable_function(edu["year"])
        myinfo_page.wait_for_timeout(5000)
    
    def test_qualifications_skill(self, logger, myinfo_page, get_my_info_data):
        # Test: Add, Edit, and Delete Skill Record
        myinfo = MyInfoPage(myinfo_page)
        skill = get_my_info_data["skill"]
        logger.info(f"Adding skill with {skill['years_exp']} years of experience")
        myinfo.add_skill(skill["years_exp"])
        myinfo_page.wait_for_timeout(5000)
        logger.info(f"Editing skill experience to: {skill['years_exp']} years")
        myinfo.edit_skill(skill["years_exp"])
        myinfo_page.wait_for_timeout(5000)
        logger.info("Deleting skill record")
        myinfo.delete_reusable_function(skill["years_exp"])
        myinfo_page.wait_for_timeout(5000)
    
    def test_qualifications_language(self, logger, myinfo_page, get_my_info_data):
        # Test: Add and Delete Language
        myinfo = MyInfoPage(myinfo_page)
        logger.info("Adding language")
        myinfo.add_language()
        myinfo_page.wait_for_timeout(5000)
        logger.info("Deleting language")
        myinfo.delete_language()
    #
    def test_memberships(self, logger, myinfo_page, get_my_info_data):
        # Test: Add, Edit, and Delete Membership record
        myinfo = MyInfoPage(myinfo_page)
        
        # Navigate to Memberships section
        logger.info("Opening Memberships tab")
        myinfo.open_memberships()
        mem = get_my_info_data["membership"]
        
        # Add new membership record
        logger.info(f"Adding membership with amount: {mem['amount']}")
        myinfo.add_membership(mem["amount"])
        myinfo_page.wait_for_timeout(5000)
        
        # Edit the membership record
        logger.info("Editing membership record")
        myinfo.edit_membership()
        myinfo_page.wait_for_timeout(5000)
        
        # Delete the membership record
        logger.info(f"Deleting membership: {mem['name']}")
        myinfo.delete_reusable_function(mem["name"])
    #     myinfo_page.wait_for_timeout(5000)
    #
    # def test_add_file_attachment(self, logger, myinfo_page, get_my_info_data):
    #     myinfo = MyInfoPage(myinfo_page)
    #     myinfo.add_attachment()
    #     myinfo_page.wait_for_timeout(15000)




