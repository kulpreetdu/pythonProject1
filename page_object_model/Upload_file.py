from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Upload_page:
    f_name_xpath="//input[@id='SearchFirstName']"
    search_button_xpath="//button[@id='search-customers']"
    send_check_xpath="//input[@id='SendEmail_SendImmediately']"
    date_xpath="//input[@id='SendEmail_DontSendBeforeDate']"
    edit_search_xpath="//table[@id='customers-grid']//tbody//tr[@class='odd'][1]//a[@class='btn btn-default']"
    back_to_cust_xpath="//a[contains(text(),'back to customer list')]"
    send_email_button_xpath="//button[@class='btn btn-success']"
    sub_email_xpath="//input[@id='SendEmail_Subject']"
    body_email_xpath="//textarea[@id='SendEmail_Body']"
    send_email_xpath="//form[@action='/Admin/Customer/SendEmail']//div[@class='modal-footer']/button"

    def __init__(self, driver):
        self.driver = driver

    def f_name_click(self,f_name):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.f_name_xpath))).clear()
        self.driver.find_element(By.XPATH,self.f_name_xpath).send_keys(f_name)

    def search_but_click(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.search_button_xpath)))
        self.driver.find_element(By.XPATH,self.search_button_xpath)

    def send_click(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.send_check_xpath)))
        self.driver.find_element(By.XPATH,self.send_check_xpath).click()

    def date_value(self,date_value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.date_xpath))).clear()
        self.driver.find_element(By.XPATH,self.date_xpath).send_keys(date_value)

    def edit_search_click(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.edit_search_xpath)))
        self.driver.find_element(By.XPATH,self.edit_search_xpath).click()

    def back_to_cust_click(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.back_to_cust_xpath)))
        self.driver.find_element(By.XPATH,self.back_to_cust_xpath).click()

    def send_email_button_click(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.send_email_button_xpath)))
        self.driver.find_element(By.XPATH,self.send_email_button_xpath).click()

    def sub_email_value(self,email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.sub_email_xpath))).clear()
        self.driver.find_element(By.XPATH,self.sub_email_xpath).send_keys(email)

    def body_email_value(self,body_email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.body_email_xpath))).clear()
        self.driver.find_element(By.XPATH,self.body_email_xpath).send_keys(body_email)

    def send_email_click(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.send_email_xpath)))
        self.driver.find_element(By.XPATH, self.send_email_xpath).click()
