from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver

class SafeClick:

    def __init__(self,driver:WebDriver):
        self.driver=driver

    def safe_click(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",element)
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element)).click()
        except:
            self.driver.execute_script("arguments[0].click();", element)