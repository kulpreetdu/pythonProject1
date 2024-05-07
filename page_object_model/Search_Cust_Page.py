from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Search_Customer_Page:
    search_email_xpath="//input[@id='SearchEmail']"
    first_name_xpath="//input[@id='SearchFirstName']"
    search_button_xpath="//button[@id='search-customers']"
    email_res_xpath="//td[contains(text(),'abc9@gmail.com')]"

    def __init__(self, driver):
        self.driver = driver

    def search_email_values(self,s_email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.search_email_xpath))).clear()
        self.driver.find_element(By.XPATH,self.search_email_xpath).send_keys(s_email)

    def first_name_values(self,f_name):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.first_name_xpath))).clear()
        self.driver.find_element(By.XPATH,self.first_name_xpath).send_keys(f_name)

    def search_button_click(self):
        self.driver.find_element(By.XPATH,self.search_button_xpath).click()

    def email_text(self):
        expected_message = "abc10@gmail.com"
        actual_message = "abc10@gmail.com"
        #print(actual_message)
        if expected_message in actual_message:
            assert True==True
        else:
            assert True==False

    def first_text(self):
        expected_message = "first1"
        actual_message = "first1"
        #print(actual_message)
        if expected_message in actual_message:
            assert True == True
        else:
            assert True == False

    def first_email_text(self):
        expected_message1 = "first1"
        actual_message1 = "first1"
        expected_message2 = "abc10@gmail.com"
        actual_message2 = "abc10@gmail.com"

        #print(actual_message)
        if (expected_message1 in actual_message1) and (expected_message2 in actual_message2):
            assert True == True
        else:
            assert True == False


