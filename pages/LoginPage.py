from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    login_to_your_account_text=(By.XPATH,"//h2[text()='Login to your account']")
    login_email=(By.CSS_SELECTOR,"input[data-qa='login-email']")
    login_password=(By.CSS_SELECTOR,"input[data-qa='login-password']")
    login_button=(By.CSS_SELECTOR,"button[data-qa='login-button']")
    signup_name=(By.CSS_SELECTOR,"input[data-qa='signup-name']")
    signup_email=(By.CSS_SELECTOR,"input[data-qa='signup-email']")
    signup_button=(By.CSS_SELECTOR,"button[data-qa='signup-button']")
    account_already_exists_text=(By.XPATH,"//p[text()='Email Address already exist!']")
    wrong_email_password_text=(By.XPATH,"//p[text()='Your email or password is incorrect!']")
    required_fields=(By.CSS_SELECTOR,"input[required]")
    incorrect_email_text=(By.XPATH,"//p[text()='Your email or password is incorrect!']")

    def __init__(self,driver:WebDriver):
        self.driver=driver

    def enter_login_details(self,**kwargs):
        fields={
            'email':self.login_email,
            'password':self.login_password
        }

        for i,j in kwargs.items():
            if i in fields:
                self.driver.find_element(*fields[i]).send_keys(j)

        # self.driver.find_element(*self.login_email).send_keys(email)
        # self.driver.find_element(*self.login_password).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def login_to_your_account_text_visibility(self):
        # return self.driver.find_element(*self.login_to_your_account_text).is_displayed()
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.login_to_your_account_text)).is_displayed()

    def enter_signup_details(self,name,email):
        self.driver.find_element(*self.signup_name).send_keys(name)
        self.driver.find_element(*self.signup_email).send_keys(email)

    def click_signup_button(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.signup_button)).click()
        # self.driver.find_element(*self.signup_button).click()

    def account_already_exists_text_visibility(self):
        wait=WebDriverWait(self.driver,10)
        return wait.until(EC.presence_of_element_located(self.account_already_exists_text)).is_displayed()

    def wrong_email_password_text_visibility(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.wrong_email_password_text)).is_displayed()

    def get_login_pass_field_filled_status(self):
        email=self.driver.find_element(*self.login_email)
        password=self.driver.find_element(*self.login_password)

        return email.get_attribute('value')=='' or password.get_attribute('value')==''

    def incorrect_email_text_visibility(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.incorrect_email_text)).is_displayed()












