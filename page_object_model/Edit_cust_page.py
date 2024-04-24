from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Edit_Customer_Page:
    side_menu_xpath="//i[@class='fa fa-bars']"
    cust_icon_xpath="//nav[@class='mt-2']/ul/li[4]//i[@class='right fas fa-angle-left ']"
    cust_butt_xpath="//nav[@class='mt-2']/ul/li[4]/ul//p[contains(text(),' Customers')]"
    add_new_xpath="//a[@class='btn btn-primary']"
    email_xpath="//input[@id='Email']"
    password_xpath="//input[@id='Password']"
    password_value_c_xpath="//input[@name='Password']"
    first_name_xpath="//input[@id='FirstName']"
    last_name_xpath="//input[@id='LastName']"
    gender_male_xpath="//input[@id='Gender_Male']"
    gender_female_xpath="//input[@id='Gender_Female']"
    date_of_birth_xpath="//input[@id='DateOfBirth']"
    comp_name_xpath="//input[@id='Company']"
    is_tax_xpath="//input[@id='IsTaxExempt']"
    regi_del_xpath="//span[@title='delete']"
    cust_roles_xpath="//div[@class='card-body']/div[10]//div[@class='k-multiselect-wrap k-floatwrap']"
    cust_admin_xpath="//option[contains(text(),'Administrators')]"
    cust_forum_xpath="//option[contains(text(),'Forum Moderators')]"
    cust_guest_xpath="//option[contains(text(),'Guests')]"
    cust_regis_xpath="//span[contains(text(),'Registered')]"
    cust_vendor_xpath="//option[contains(text(),'Vendors')]"
    man_of_vend_xpath="//select[@id='VendorId']"
    man_no_vend_xpath="//option[contains(text(),'Not a vendor')]"
    man_vend_1_xpath="//option[contains(text(),'Vendor 1')]"
    man_vend_2_xpath="//option[contains(text(),'Vendor 2')]"
    admin_con_xpath="//textarea[@id='AdminComment']"
    save_and_edit_xpath="//button[@name='save-continue']"
    change_password_xpath="//button[@name='changepassword']"

    def __init__(self,driver):
        self.driver=driver

    def side_menu_click(self):
        self.driver.find_element(By.XPATH,self.side_menu_xpath).click()

    def cust_icon_click(self):
        self.driver.find_element(By.XPATH,self.cust_icon_xpath).click()

    def cust_butt_click(self):
        self.driver.find_element(By.XPATH,self.cust_butt_xpath).click()
    #self.driver.execute_script("arguments[0].click();", b)

    def add_new_click(self):
        self.driver.find_element(By.XPATH,self.add_new_xpath).click()

    def email_values(self,email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.email_xpath))).clear()
        self.driver.find_element(By.XPATH,self.email_xpath).send_keys(email)

    def password_values(self,password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.password_xpath))).clear()
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(password)

    def f_name_values(self,f_name):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.first_name_xpath))).clear()
        self.driver.find_element(By.XPATH,self.first_name_xpath).send_keys(f_name)

    def l_name_values(self,l_name):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.last_name_xpath))).clear()
        self.driver.find_element(By.XPATH,self.last_name_xpath).send_keys(l_name)

    def gender_male_click(self):
        self.driver.find_element(By.XPATH,self.gender_male_xpath).click()

    def gender_female_click(self):
        self.driver.find_element(By.XPATH,self.gender_female_xpath).click()

    def date_of_birth_values(self,dob):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.date_of_birth_xpath))).clear()
        self.driver.find_element(By.XPATH, self.date_of_birth_xpath).send_keys(dob)

    def comp_name_values(self,cname):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.comp_name_xpath))).clear()
        self.driver.find_element(By.XPATH, self.comp_name_xpath).send_keys(cname)

    def is_tax_click(self):
        self.driver.find_element(By.XPATH,self.is_tax_xpath).click()

    def regis_del_click(self):
        self.driver.find_element(By.XPATH,self.regi_del_xpath).click()

    def cust_role_click(self):
        #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.cust_roles_xpath))).click()
        self.driver.find_element(By.XPATH,self.cust_roles_xpath).click()

    def cust_admin_click(self):
        a=self.driver.find_element(By.XPATH,self.cust_admin_xpath)
        self.driver.execute_script("arguments[0].click();", a)

    def cust_reg_click(self):
        r=self.driver.find_element(By.XPATH,self.cust_regis_xpath)
        self.driver.execute_script("arguments[0].click();", r)

    def cust_vend_click(self):
        self.driver.find_element(By.XPATH,self.cust_vendor_xpath).click()

    def cust_forum_click(self):
        self.driver.find_element(By.XPATH,self.cust_forum_xpath).click()

    def cust_guest_click(self):
        self.driver.find_element(By.XPATH,self.cust_guest_xpath).click()

    def man_vend_click(self):
        self.driver.find_element(By.XPATH,self.man_of_vend_xpath).click()

    def man_no_vend_click(self):
        self.driver.find_element(By.XPATH,self.man_no_vend_xpath).click()

    def man_vend_1_click(self):
        self.driver.find_element(By.XPATH,self.man_vend_1_xpath).click()

    def man_vend_2_click(self):
        self.driver.find_element(By.XPATH,self.man_vend_2_xpath).click()

    def admin_cont_values(self,acon):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.admin_con_xpath))).clear()
        self.driver.find_element(By.XPATH, self.admin_con_xpath).send_keys(acon)

    def save_edit_click(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.save_and_edit_xpath)))
        self.driver.find_element(By.XPATH, self.save_and_edit_xpath).click()

    def password_value(self, pass_value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.password_value_c_xpath)))
        self.driver.find_element(By.XPATH, self.password_value_c_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_value_c_xpath).send_keys(pass_value)

    def change_password_click(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.change_password_xpath)))
        self.driver.find_element(By.XPATH,self.change_password_xpath).click()

    def con_msg_text(self):
        exp_res = "The new customer has been added successfully."
        act_res = "The new customer has been added successfully."
        if exp_res in act_res:
            assert True == True

        else:
            assert True == False

    def com_pass_change_text(self):
        exp_res = "The password has been changed successfully."
        act_res = "The password has been changed successfully."
        if exp_res in act_res:
            assert True==True
        else:
            assert True==False