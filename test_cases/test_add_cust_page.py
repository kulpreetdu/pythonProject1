import time
import random
from page_object_model.Login_Page import Login_Page
from utilities.readProperties import ReadConfig
from page_object_model.Add_Cus_Page import Add_Customer_Page
from utilities.customlogger import LogGen
import pytest

class Test_001_Add_Cust:
    base_url = ReadConfig.get_url()
    username1 = ReadConfig.get_username1()
    password1 = ReadConfig.get_password1()
    rand_num=random.randint(1, 10)
    email="abc"+str(rand_num)+"@gmail.com"
    password_val="12345"
    f_name="first"
    l_name="last"
    dob="02/22/1995"
    cname="cname"
    acon="acon"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_add_cust(self,setup):
        self.logger.info("*****Test_01_add_customer*****")
        self.logger.info("*****Veriying Add Customer test cases*****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("*****Starting logging test case*****")
        self.lp = Login_Page(self.driver)
        self.lp.username1_values(self.username1)
        time.sleep(1)
        self.lp.password1_values(self.password1)
        time.sleep(1)
        self.lp.login_click()
        self.logger.info("*****Logging test case successful*****")
        time.sleep(1)
        self.logger.info("*****Starting add customer test case*****")
        self.ad=Add_Customer_Page(self.driver)
        #self.ad.side_menu_click()
        self.ad.cust_icon_click()
        time.sleep(1)
        self.ad.cust_butt_click()
        time.sleep(1)
        self.ad.add_new_click()
        time.sleep(1)
        self.ad.email_values(self.email)
        time.sleep(1)
        self.ad.password_values(self.password_val)
        time.sleep(1)
        self.ad.f_name_values(self.f_name)
        time.sleep(1)
        self.ad.l_name_values(self.l_name)
        time.sleep(1)
        self.ad.gender_male_click()
        time.sleep(1)
        self.ad.date_of_birth_values(self.dob)
        time.sleep(1)
        self.ad.comp_name_values(self.cname)
        time.sleep(1)
        self.ad.is_tax_click()
        time.sleep(1)
        #self.ad.regis_del_click()
        #time.sleep(1)
        #self.ad.cust_role_click()
        #time.sleep(1)
        #self.ad.cust_reg_click()
        #time.sleep(1)
        self.ad.man_vend_click()
        time.sleep(1)
        self.ad.man_vend_1_click()
        time.sleep(1)
        self.ad.admin_cont_values(self.acon)
        time.sleep(1)
        self.ad.save_click()
        time.sleep(1)
        self.ad.msg_text()
        time.sleep(1)
        self.lp.logout_click()
        self.logger.info("*****Logout test case successful*****")
        self.driver.close()
        self.logger.info("*****Driver closed test case*****")

