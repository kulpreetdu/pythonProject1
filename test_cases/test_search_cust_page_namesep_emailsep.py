import time
from page_object_model.Login_Page import Login_Page
from utilities.readProperties import ReadConfig
from page_object_model.Add_Cus_Page import Add_Customer_Page
from page_object_model.Search_Cust_Page import Search_Customer_Page
from utilities.customlogger import LogGen
import pytest


class Test_001_Search_Cust_By_Namesep_Emailsep:
    base_url = ReadConfig.get_url()
    username1 = ReadConfig.get_username1()
    password1 = ReadConfig.get_password1()
    s_email="abc10@gmail.com"
    f_name="first1"
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_Search_cust_emailsep(self, setup):
        self.logger.info("*****Test_01_search_customer_email*****")
        self.logger.info("*****Veriying Search Customer by email test cases*****")
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
        self.ad = Add_Customer_Page(self.driver)
        # self.ad.side_menu_click()
        self.ad.cust_icon_click()
        time.sleep(1)
        self.ad.cust_butt_click()
        self.logger.info("*****add customer test case successful*****")
        time.sleep(1)
        self.logger.info("*****Starting search customer test case*****")
        self.sr = Search_Customer_Page(self.driver)
        self.sr.search_email_values(self.s_email)
        time.sleep(1)
        self.sr.search_button_click()
        time.sleep(2)
        self.sr.email_text()
        time.sleep(1)
        self.logger.info("*****Search customer test case successful*****")
        self.lp.logout_click()
        self.logger.info("*****loggout test case*****")
        self.driver.close()
        self.logger.info("*****Driver closed test case*****")

        @pytest.mark.regression
        def test_Search_cust_namesep(self, setup):
            self.logger.info("*****Test_01_search_customer_by_name*****")
            self.logger.info("*****Veriying Search Customer by name test cases*****")
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
            self.ad = Add_Customer_Page(self.driver)
            # self.ad.side_menu_click()
            self.ad.cust_icon_click()
            time.sleep(1)
            self.ad.cust_butt_click()
            self.logger.info("*****add customer test case successful*****")
            time.sleep(1)
            self.logger.info("*****Starting search customer test case*****")
            self.sr = Search_Customer_Page(self.driver)
            self.sr.first_name_values(self.f_name)
            time.sleep(1)
            self.sr.search_button_click()
            time.sleep(2)
            self.sr.first_text()
            time.sleep(1)
            self.logger.info("*****Search customer test case successful*****")
            self.lp.logout_click()
            self.logger.info("*****loggout test case*****")
            self.driver.close()
            self.logger.info("*****Driver closed test case*****")
