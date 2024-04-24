import time
from page_object_model.Login_Page import Login_Page
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
from page_object_model.Edit_cust_page import Edit_Customer_Page
import pytest

class Test_01_Edit_Cust:
    base_url=ReadConfig.get_url()
    username1=ReadConfig.get_username1()
    password1=ReadConfig.get_password1()
    email_val="test_evev@gmail.com"
    pass_val="password_testing_va"
    f_name_val="test_evavf"
    l_name_val="test_evavl"
    date_of_birth_val="04/24/2024"
    c_name_val="c_name"
    admin_cont_val="admin_cont"
    pass_edit_value="password_test_chang"

    logger = LogGen.loggen()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_01_edit(self,setup):
        self.logger.info("*****Test_01_edit_customer_page*****")
        self.logger.info("*****Veriying_Edit_Customer_page_test_cases*****")
        self.driver=setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("*****Login_test_started_successfully*****")
        self.lp=Login_Page(self.driver)
        self.lp.username1_values(self.username1)
        self.lp.password1_values(self.password1)
        self.logger.info("*****Login_successfully_performed*****")
        self.lp.login_click()

        self.logger.info("*****Creation_of_Edit_customer_page*****")
        self.ed=Edit_Customer_Page(self.driver)
        self.ed.cust_icon_click()
        time.sleep(2)
        self.ed.cust_butt_click()
        time.sleep(2)
        self.ed.add_new_click()
        time.sleep(2)
        self.ed.email_values(self.email_val)
        time.sleep(2)
        self.ed.password_value(self.pass_val)
        time.sleep(2)
        self.ed.f_name_values(self.f_name_val)
        time.sleep(2)
        self.ed.l_name_values(self.l_name_val)
        time.sleep(2)
        self.ed.gender_male_click()
        time.sleep(2)
        self.ed.date_of_birth_values(self.date_of_birth_val)
        time.sleep(2)
        self.ed.comp_name_values(self.c_name_val)
        time.sleep(2)
        self.ed.is_tax_click()
        time.sleep(2)
        self.ed.man_vend_click()
        time.sleep(2)
        self.ed.man_vend_1_click()
        time.sleep(2)
        self.logger.info("*****Successfully_edit_the_customer*****")
        self.ed.save_edit_click()
        time.sleep(2)
        self.ed.password_value(self.pass_edit_value)
        time.sleep(2)
        self.ed.change_password_click()
        time.sleep(2)
        self.ed.con_msg_text()
        time.sleep(2)
        self.ed.com_pass_change_text()
        time.sleep(2)
        self.logger.info("*****Successfully_logout*****")
        self.lp.logout_click()
        time.sleep(2)
        self.logger.info("*****driver_closed*****")
        self.driver.close()





