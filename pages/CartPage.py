import re
from weakref import finalize

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    click_here_button=(By.XPATH,"//u[text()='here']")
    home_button=(By.XPATH,"//a[text()='Home']")
    proceed_to_checkout_button=(By.XPATH,"//a[text()='Proceed To Checkout']")
    register_login_button=(By.XPATH,"//u[text()='Register / Login']")
    continue_on_cart_button=(By.CSS_SELECTOR,"button[data-dismiss='modal']")
    cart_delete_button=(By.XPATH,"//td[@class='cart_delete']")
    product_descriptions=(By.CSS_SELECTOR,"td.cart_description")
    delete_item_button=(By.CSS_SELECTOR,"a.cart_quantity_delete")
    product_row=(By.XPATH,"//tbody//tr")
    table_column_data=(By.XPATH,"//tbody//tr//td")
    cart_empty_text=(By.XPATH,"//b[text()='Cart is empty!']")
    quantity_text=(By.CSS_SELECTOR,"button.disabled")
    cart_total_value_text=(By.CSS_SELECTOR,"td.cart_total")

    def __init__(self,driver:WebDriver):
        self.driver=driver

    def click_click_here_button(self):
        self.driver.find_element(*self.click_here_button).click()

    def click_home_button(self):
        self.driver.find_element(*self.home_button).click()

    def click_proceed_to_checkout_button(self):
        # self.driver.find_element(*self.proceed_to_checkout_button).click()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.proceed_to_checkout_button)).click()

    def click_register_login_button(self):
        self.driver.find_element(*self.register_login_button).click()

    def register_login_text_visibility(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.register_login_button)).is_displayed()

    def click_continue_to_cart_button(self):
        self.driver.find_element(*self.continue_on_cart_button).click()

    def click_cart_delete_button(self):
        self.driver.find_element(*self.cart_delete_button).click()

    def product_description_text(self):
        descriptions = self.driver.find_elements(*self.product_descriptions)
        items=[]
        for i in descriptions:
            items.append(WebDriverWait(self.driver, 10).until(EC.visibility_of(i)).text)
        return items

        # return WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.product_descriptions)).text
        # return self.driver.find_element(*self.product_descriptions).text

    def product_description_visibility(self):
        descriptions=self.driver.find_elements(*self.product_descriptions)
        for i in descriptions:
            return WebDriverWait(self.driver,10).until(EC.visibility_of(i)).is_displayed()

        # return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.product_descriptions)).is_displayed()

    def cart_empty_text_visibility(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.cart_empty_text)).is_displayed()

    def click_delete_item_button(self,product_name):
        # products_in_cart=self.driver.find_elements(*self.product_descriptions)
        rows=self.driver.find_elements(*self.product_row)
        # columns=self.driver.find_elements(*self.table_column_data)

        for i in rows:
            if product_name.lower() in i.text.lower():
                element=i.find_element(*self.delete_item_button)
                WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(element)).click()
                break

    def quantity_text_visibility(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.quantity_text)).text

    def get_cart_total_value(self):
        # prices=self.driver.find_elements(*self.cart_total_value_text)
        # prices_list=[]
        # for i in prices:
        #     prices_list.append(WebDriverWait(self.driver, 10).until(EC.visibility_of(i)).text)
        # return prices_list
        elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.cart_total_value_text)
        )

        prices_list = []
        for el in elements:
            text = el.text
            price = int(re.sub(r'\D', '', text))
            prices_list.append(price)

        return prices_list

    def get_cart_description_text(self,product_name):
        rows=self.driver.find_elements(*self.product_row)

        for i in rows:
            if product_name.lower() in i.text.lower():
                description=i.find_element(*self.product_descriptions)
                return description.text

