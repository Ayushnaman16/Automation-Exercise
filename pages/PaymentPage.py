from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaymentPage:

    payment_text=(By.XPATH,"//h2[text()='Payment']")
    name_on_card=(By.CSS_SELECTOR,"input[name='name_on_card']")
    card_number=(By.CSS_SELECTOR,"input[name='card_number']")
    cvc=(By.CSS_SELECTOR,"input[name='cvc']")
    expiry_month=(By.CSS_SELECTOR,"input[name='expiry_month']")
    expiry_year=(By.CSS_SELECTOR,"input[name='expiry_year']")
    pay_confirm_button=(By.CSS_SELECTOR,"button[data-qa='pay-button']")
    order_placed_text=(By.XPATH,"//b[text()='Order Placed!']")
    download_invoice_button=(By.CSS_SELECTOR,"a[href='/download_invoice/500']")
    continue_button=(By.CSS_SELECTOR,"a[data-qa='continue-button']")
    

    def __init__(self,driver:WebDriver):
        self.driver=driver

    def enter_card_details(self,name,cardnumber,cvc,month,year):
        self.driver.find_element(*self.name_on_card).send_keys(name)
        self.driver.find_element(*self.card_number).send_keys(cardnumber)
        self.driver.find_element(*self.cvc).send_keys(cvc)
        self.driver.find_element(*self.expiry_month).send_keys(month)
        self.driver.find_element(*self.expiry_year).send_keys(year)

    def click_pay_confirm_button(self):
        self.driver.find_element(*self.pay_confirm_button).click()

    def order_placed_text_visibility(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.order_placed_text)).is_displayed()



