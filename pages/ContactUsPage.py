from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class ContactUsPage:

    name=(By.CSS_SELECTOR,"input[data-qa='name']")
    email=(By.CSS_SELECTOR,"input[data-qa='email']")
    subject=(By.CSS_SELECTOR,"input[data-qa='subject']")
    message_box=(By.CSS_SELECTOR,"textarea[data-qa='message']")
    upload_button=(By.CSS_SELECTOR,"input[name='upload_file']")
    submit_button=(By.CSS_SELECTOR,"input[name='submit']")
    contact_us_text=(By.CSS_SELECTOR,"div.col-sm-12")
    success_message_text=(By.CSS_SELECTOR,"div.status.alert.alert-success")

    def __init__(self,driver:WebDriver):
        self.driver=driver

    def contact_us_text_visibility(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.contact_us_text)).is_displayed()

    def success_message_text_visibility(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.success_message_text)).is_displayed()

    def enter_contact_us_details(self,**kwargs):
        fields={
            'name':self.name,
            'email':self.email,
            'subject':self.subject,
            'message':self.message_box
        }

        for i,j in kwargs.items():
            if i in fields:
                self.driver.find_element(*fields[i]).send_keys(j)

    def click_submit_button(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.submit_button)).click()

    def handling_alert(self):
        alert=self.driver.switch_to.alert
        alert.accept()

    def upload_file_functionality(self,file):
        # file='D:\\Automation Excercise\\testdata\\AutomationExercise_60_Detailed_TestCases.xlsx'
        self.driver.find_element(*self.upload_button).send_keys(file)




