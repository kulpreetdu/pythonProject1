from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Dashboard:
    nop_comm_news_plus_xpath = "//div[@id='nopcommerce-news-box']/div[1]/div[2]/button"
    nop_comm_news_minus_xpath = "//div[@id='nopcommerce-news-box']/div[1]/div[2]/button"
    non_comm_link_xpath="//section[@class='content']/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[1]/a"
    non_com_rem_key_site_url_xpath_="//input[@name='product_attribute_1']"
    non_com_rem_key_add_to_cart_xpath="//input[@id='add-to-cart-button-5892']"
    server_rem_cont_xpath= "//div[@data-productid='5898']//div[4]/a"
    request_type_xpath = "//select[@class='form-control valid']"
    request_type_0_xpath="//option[@value='0']"
    request_type_1_xpath ="//option[@value='1']"
    request_type_2_xpath="//option[@value='2']"
    request_type_3_xpath="//option[@value='3']"
    request_type_4_xpath="//option[@value='4']"
    your_name_xpath="//input[@name='FullName']"
    your_email_xpath="//input[@name='Email']"
    enquiry_xpath="//textarea[@name='Enquiry']"
    robot_check_xpath="//span[@role='checkbox']/div[1]"
    submit_xpath="//input[@type='submit']"

    def __init__(self,driver):
        self.driver=driver
    def nop_com_new_plus_click(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.nop_comm_news_plus_xpath)))
        self.driver.find_element(By.XPATH,self.nop_comm_news_plus_xpath).click()

    def nop_com_new_minus_click(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.nop_comm_news_minus_xpath)))
        self.driver.find_element(By.XPATH,self.nop_comm_news_minus_xpath).click()

    def non_com_link_click(self):
        WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.XPATH, self.non_comm_link_xpath)))
        link = self.driver.find_element(By.XPATH,self.non_comm_link_xpath)
        self.driver.execute_script("arguments[0].click();", link)

    def nop_com_rem_key_value(self,url_value):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.non_com_rem_key_site_url_xpath_))).clear()
        self.driver.find_element(By.XPATH,self.non_com_rem_key_site_url_xpath_).send_keys(url_value)

    def nop_com_rem_key_add_click(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.non_com_rem_key_add_to_cart_xpath)))
        self.driver.find_element(By.XPATH,self.non_com_rem_key_add_to_cart_xpath).click()

    def ser_rem_cont_us_click(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.server_rem_cont_xpath)))
        self.driver.find_element(By.XPATH,self.server_rem_cont_xpath).click()

    def req_type_click(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.request_type_xpath)))
        self.driver.find_element(By.XPATH,self.request_type_xpath).click()

    def req_type_1_click(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.request_type_1_xpath)))
        self.driver.find_element(By.XPATH,self.request_type_1_xpath).click()

    def your_name_value(self, name):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.your_name_xpath))).clear()
        self.driver.find_element(By.XPATH,self.your_name_xpath).send_keys(name)

    def your_email_value(self, email):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.your_email_xpath))).clear()
        self.driver.find_element(By.XPATH,self.your_email_xpath).send_keys(email)

    def enquiry_value(self,enq_value):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.enquiry_xpath))).clear()
        self.driver.find_element(By.XPATH,self.enquiry_xpath).send_keys(enq_value)

    def robot_click(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.robot_check_xpath)))
        self.driver.find_element(By.XPATH,self.robot_check_xpath).click()

    def submit_click(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self.submit_xpath)))
        self.driver.find_element(By.XPATH,self.submit_xpath).click()










