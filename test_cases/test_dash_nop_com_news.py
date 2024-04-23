from page_object_model.Dashboard_page import Dashboard
from page_object_model.Login_Page import Login_Page
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
import pytest
import time
class Test_01_Dash_Nop_Com_News:
    base_url = ReadConfig.get_url()
    page2_url = ReadConfig.get_page2_url()
    username1 = ReadConfig.get_username1()
    password1 = ReadConfig.get_password1()
    url_value="www.test.com"

    logger = LogGen.loggen()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_dash_nop_com_news(self,setup):
        self.logger.info("*****Test_01_dash_nop_com*****")
        self.logger.info("*****Clicking_the_nop_commerce_link*****")
        self.driver=setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("*****Test_01_Login*****")
        self.logger.info("*****Login_started*****")
        self.lp=Login_Page(self.driver)
        self.lp.username1_values(self.username1)
        time.sleep(2)
        self.lp.password1_values(self.password1)
        time.sleep(2)
        self.lp.login_click()
        time.sleep(2)
        self.logger.info("*****Test_01_dash_nop_com_click*****")

        self.db=Dashboard(self.driver)

        self.db.nop_com_new_plus_click()
        time.sleep(2)
        self.db.nop_com_new_minus_click()
        time.sleep(2)

        self.driver.get(self.page2_url)
        self.driver.maximize_window()
        #self.db.nop_com_new_minus_click()
        #time.sleep(2)
        #self.db.non_com_link_click()
        #time.sleep(2)
        self.db.nop_com_rem_key_value(self.url_value)
        time.sleep(2)
        self.db.nop_com_rem_key_add_click()
        time.sleep(2)
        self.driver.back()
        #self.driver.execute_script("window.history.go(-1)")
        self.driver.back()
        time.sleep(2)
        #self.driver.execute_script("window.history.go(-1)")
        time.sleep(2)
        """
        db.ser_rem_cont_us_click()
        time.sleep(2)
        """
        self.logger.info("*****Logout_application*****")
        self.lp.logout_click()
        self.logger.info("*****Driver_close*****")
        self.driver.quit()