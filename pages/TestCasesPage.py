from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestCasesPage:

    list_of_test_cases_text=(By.CSS_SELECTOR,"span[style='color: red;']")

    def __init__(self,driver:WebDriver):
        self.driver=driver

    def list_of_test_cases_text_visibility(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.list_of_test_cases_text)).is_displayed()



