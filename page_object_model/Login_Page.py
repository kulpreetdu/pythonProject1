from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Login_Page:
    username1_xpath = "//*[contains(@id,'Email')]"
    password1_xpath = "//*[contains(@id,'Password')]"
    login_xpath = "//*[contains(text(),'Log in')]"
    logout_xpath = "//*[contains(text(),'Logout')]"

    def __init__(self, driver):
        self.driver = driver

    def username1_values(self,username1):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.username1_xpath))).clear()
        self.driver.find_element(By.XPATH,self.username1_xpath).send_keys(username1)

    def password1_values(self,password1):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.password1_xpath))).clear()
        self.driver.find_element(By.XPATH,self.password1_xpath).send_keys(password1)

    def username2_values(self,username2):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.username1_xpath))).clear()
        self.driver.find_element(By.XPATH,self.username1_xpath).send_keys(username2)

    def password2_values(self,password2):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.password1_xpath))).clear()
        self.driver.find_element(By.XPATH,self.password1_xpath).send_keys(password2)

    def username3_values(self,username3):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.username1_xpath))).clear()
        self.driver.find_element(By.XPATH,self.username1_xpath).send_keys(username3)

    def password3_values(self,password3):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.password1_xpath))).clear()
        self.driver.find_element(By.XPATH,self.password1_xpath).send_keys(password3)

    def username4_values(self,username4):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.username1_xpath))).clear()
        self.driver.find_element(By.XPATH,self.username1_xpath).send_keys(username4)

    def password4_values(self,password4):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.password1_xpath))).clear()
        self.driver.find_element(By.XPATH,self.password1_xpath).send_keys(password4)

    def login_click(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.login_xpath))).click()

    def logout_click(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.logout_xpath))).click()
