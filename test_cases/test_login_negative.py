from page_object_model.Login_Page import Login_Page
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
import pytest


class Test_01_Login_Negative:
    base_url = ReadConfig.get_url()
    username1 = ReadConfig.get_username1()
    password1 = ReadConfig.get_password1()
    username2 = ReadConfig.get_username2()
    password2 = ReadConfig.get_password2()
    username3 = ReadConfig.get_username3()
    password3 = ReadConfig.get_password3()
    username4 = ReadConfig.get_username4()
    password4 = ReadConfig.get_password4()

    logger=LogGen.loggen()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login_negative1(self, setup):
        self.logger.info("*****Test_02_login*****")
        self.logger.info("*****Veriying logging test case*****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("*****Starting logging test case*****")
        self.lp = Login_Page(self.driver)
        self.lp.username2_values(self.username2)
        self.lp.password2_values(self.password2)
        self.lp.login_click()
        self.logger.info("*****Negative1 Logging test case successful*****")
        print("negative1 scenario added successfully")
        self.logger.info("*****Test_02_login*****")
        self.logger.info("*****Veriying logging test case*****")
        self.logger.info("*****Starting logging test case*****")
        self.lp.username3_values(self.username3)
        self.lp.password3_values(self.password3)
        self.lp.login_click()
        self.logger.info("*****Negative2 Logging test case successful*****")
        print("negative2 scenario added successfully")
        self.logger.info("*****Test_03_login*****")
        self.logger.info("*****Veriying logging test case*****")
        self.logger.info("*****Starting logging test case*****")
        self.lp.username4_values(self.username4)
        self.lp.password4_values(self.password4)
        self.lp.login_click()
        self.logger.info("*****Negative3 Logging test case successful*****")
        print("negative3 scenario added successfully")
        self.driver.close()
        self.logger.info("*****Driver closed successful*****")
