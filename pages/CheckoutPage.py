from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By

class CheckoutPage:

    review_order_text=(By.XPATH,"//h2[text()='Review Your Order']")
    cart_total_amount=(By.XPATH,"(//p[@class='cart_total_price'])[2]")
    place_order_button=(By.CSS_SELECTOR,"a[href='/payment']")
    your_delivery_address_text=(By.CSS_SELECTOR,"ul.address.item.box")
    product_rows=(By.XPATH,"//tbody//tr")
    product_descriptions=(By.CSS_SELECTOR,"td.cart_description")

    def __init__(self,driver:WebDriver):
        self.driver=driver

    def click_place_order_button(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.place_order_button)).click()

    def your_delivery_address_text_visibility(self):
        return WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.your_delivery_address_text)).is_displayed()

    def get_product_description_text(self,product_name):
        rows=self.driver.find_elements(*self.product_rows)

        for i in rows:
            if product_name.lower() in i.text.lower():
                description=i.find_element(*self.product_descriptions)
                return description.text

    def review_order_text_visibility(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.review_order_text)).is_displayed()



