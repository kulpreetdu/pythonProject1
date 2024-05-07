import time
from page_object_model.Login_Page import Login_Page
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
from page_object_model.Add_Cus_Page import Add_Customer_Page
from page_object_model.delete_cus_page import Delete_cust_page
from page_object_model.Upload_file import Upload_page
import pytest
import random


class Test_01_upload:
    base_url=ReadConfig.get_url()
    username1=ReadConfig.get_username1()
    password2=ReadConfig.get_password1()
    e_val=random.randint(1,10)
    p_val=random.randint(1,10)
    email_val="email_val"+str(e_val)+"@gmail.com"
    password_val="pass_val"+str(p_val)+"@gmail.com"
    f_name="test_1_fir"
    l_name="l_333_name"
    date_of_birth_val="07/05/2024"
    comp_value="cname"
    acon_val="acon"
    p_ch_val=random.randint(1,10)
    pass_val="te_st"+str(p_ch_val)+"@gmail.com"
    email_val = random.randint(1, 10)
    email_value = "email_test" + str(email_val)
    bod_email_val = random.randint(1, 10)
    bod_email_value = "body_email_test" + str(bod_email_val)

    logger=LogGen.loggen()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_01_upload_file(self, setup):
        self.driver = setup
        self.logger.info("*****Test_01_upload_file_cust*****")
        self.logger.info("*****upload_file_cust_page*****")
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("*****Test_01_upload_login_started*****")
        self.lp = Login_Page(self.driver)
        self.lp.username1_values(self.username1)
        self.lp.password1_values(self.password2)
        self.lp.login_click()
        self.logger.info("*****Login_successful*****")
        self.logger.info("*****Test_01_add_customer_login_started*****")
        self.ad=Add_Customer_Page(self.driver)
        self.ad.cust_icon_click()
        time.sleep(2)
        self.ad.cust_butt_click()
        time.sleep(2)
        self.logger.info("*****Test_01_upload_file_started*****")
        self.up=Upload_page(self.driver)
        self.up.f_name_click(self.f_name)
        time.sleep(2)
        self.up.search_but_click()
        time.sleep(2)
        self.up.edit_search_click()
        time.sleep(2)
        self.up.back_to_cust_click()
        time.sleep(2)
        self.up.f_name_click(self.f_name)
        time.sleep(2)
        self.up.search_but_click()
        time.sleep(2)
        self.up.edit_search_click()
        time.sleep(2)
        self.up.send_email_button_click()
        time.sleep(2)
        self.up.sub_email_value(self.email_value)
        time.sleep(2)
        self.up.body_email_value(self.bod_email_value)
        time.sleep(2)
        self.up.send_click()
        time.sleep(2)
        self.up.date_value(self.date_of_birth_val)
        time.sleep(2)
        self.up.send_email_click()
        time.sleep(2)
        self.logger.info("*****Test_01_upload_file_successful*****")
        self.logger.info("*****Test_01_logout*****")
        self.lp.logout_click()
        time.sleep(2)
        self.logger.info("*****Test_01_driver_closed*****")
        self.driver.close()
