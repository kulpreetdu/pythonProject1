from page_object_model.Dashboard_page import Dashboard
from page_object_model.Login_Page import Login_Page
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
import pytest
import time
class Test_01_Dash_cont_us:
    base_url=ReadConfig.get_url()
    username1=ReadConfig.get_username1()
    password1=ReadConfig.get_password1()
    page2_url=ReadConfig.get_page2_url()
    name_value = "test_name2"
    email_value = "test_email2@gmail.com"
    enquiry_value = "test_enquiry2"

    logger=LogGen.loggen()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_dash_cont_us(self,setup):
        self.logger.info("*****Test_01_dash_contact_us*****")
        self.logger.info("*****Clicking_the_contact_us*****")
        self.driver=setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("*****Test_01_Login*****")
        self.logger.info("*****Login_started*****")
        self.lp=Login_Page(self.driver)
        time.sleep(2)
        self.lp.username1_values(self.username1)
        time.sleep(2)
        self.lp.password1_values(self.password1)
        time.sleep(2)
        self.logger.info("*****successfully_login*****")
        self.lp.login_click()
        time.sleep(2)
        self.logger.info("*****Test_01_dash_nop_com_click*****")

        self.db = Dashboard(self.driver)
        self.db.nop_com_new_plus_click()
        time.sleep(2)
        self.db.nop_com_new_minus_click()
        time.sleep(2)
        self.driver.get(self.page2_url)
        self.driver.maximize_window()
        self.db.ser_rem_cont_us_click()
        time.sleep(2)
        self.db.req_type_1_click()
        time.sleep(2)
        self.db.your_name_value(self.name_value)
        time.sleep(2)
        self.db.your_email_value(self.email_value)
        time.sleep(2)
        self.db.enquiry_value(self.enquiry_value)
        time.sleep(2)
        self.db.robot_switch_frame_click()
        time.sleep(2)
        self.db.robot_click()
        time.sleep(2)
        self.db.submit_click()
        time.sleep(2)
        self.db.contact_us_text()
        self.logger.info("sucessfully_entered_value_in_contact_us_page")

        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.back(2)
        time.sleep(2)
        self.driver.back(2)
        time.sleep(2)
        self.logger.info("sucessfully_logout_page")

        self.lp.logout_click()
        time.sleep(2)


