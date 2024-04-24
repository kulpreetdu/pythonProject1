import time
from page_object_model.Login_Page import Login_Page
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
from page_object_model.delete_cus_page import Delete_cust_page
import pytest


class Test_01_delete_cust:
    base_url=ReadConfig.get_url()
    username1=ReadConfig.get_username1()
    password2=ReadConfig.get_password1()
    email_val="te_st_333@gmail.com"
    password_val="te_st_333@gmail.com"
    f_name="f_333_name"
    l_name="l_333_name"
    date_of_birth_val="04/24/2024"
    comp_value="cname"
    acon_val="acon"
    pass_val="te_st_330@gmail.com"

    logger=LogGen.loggen()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_01_delete_cust(self,setup):
        self.driver=setup
        self.logger.info("*****Test_01_delete_cust*****")
        self.logger.info("*****Deleting_cust_page*****")
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("*****Test_01_delete_login_started*****")
        self.lp=Login_Page(self.driver)
        self.lp.username1_values(self.username1)
        self.lp.password1_values(self.password2)
        self.lp.login_click()
        self.logger.info("*****Login_successful*****")
        self.db=Delete_cust_page(self.driver)
        self.logger.info("*****Creation_of_customer*****")
        self.db.cust_icon_click()
        time.sleep(2)
        self.db.cust_butt_click()
        time.sleep(2)
        self.db.add_new_click()
        time.sleep(2)
        self.db.email_values(self.email_val)
        time.sleep(2)
        self.db.password_value(self.password_val)
        time.sleep(2)
        self.db.f_name_values(self.f_name)
        time.sleep(2)
        self.db.l_name_values(self.l_name)
        time.sleep(2)
        self.db.gender_male_click()
        time.sleep(2)
        self.db.date_of_birth_values(self.date_of_birth_val)
        time.sleep(2)
        self.db.comp_name_values(self.comp_value)
        time.sleep(2)
        self.db.is_tax_click()
        time.sleep(2)
        self.db.man_vend_click()
        time.sleep(2)
        self.db.man_vend_1_click()
        time.sleep(2)
        self.db.admin_cont_values(self.acon_val)
        time.sleep(2)
        self.logger.info("*****Successfully_edit_the customer*****")
        self.db.save_edit_click()
        time.sleep(2)
        self.db.con_msg_text()
        time.sleep(2)
        self.db.password_value(self.pass_val)
        time.sleep(2)
        self.db.change_password_click()
        time.sleep(2)
        self.db.com_pass_change_text()
        time.sleep(2)
        self.logger.info("*****Successfully_updated_the_customer*****")

        #self.db.delete_click()
        #time.sleep(5)
        #self.db.close_click()
        #time.sleep(2)
        #self.db.accept_click()
        #time.sleep(2)
        self.db.con_delete_cust_text()
        time.sleep(2)
        self.lp.logout_click()
        time.sleep(2)
        self.driver.close()


