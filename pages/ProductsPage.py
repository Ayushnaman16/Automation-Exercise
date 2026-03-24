from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.SafeClickUtility import SafeClick
from selenium.webdriver.common.action_chains import ActionChains

class ProductsPage:

    all_products_text=(By.CSS_SELECTOR,"h2.title.text-center")
    search_product_bar=(By.CSS_SELECTOR,"input#search_product")
    all_products=(By.CSS_SELECTOR,"div.single-products")
    search_product_button=(By.CSS_SELECTOR,"button#submit_search")
    view_product_button=(By.XPATH,"//a[text()='View Product']")
    quantity_text=(By.XPATH,"//label[text()='Quantity:']")
    all_prices=(By.XPATH,"//div[@class='productinfo text-center']//h2")
    all_categories=(By.CSS_SELECTOR,"a[data-parent='#accordian']")
    women_categories=(By.XPATH,"//div[@id='Women']//li")
    men_categories=(By.XPATH,"//div[@id='Men']//li")
    kids_categories=(By.XPATH,"//div[@id='Kids']//li")
    brand_names=(By.CSS_SELECTOR,"div.brands-name")
    add_to_cart_button=(By.CSS_SELECTOR,"a.btn.btn-default.add-to-cart")
    # added_to_Cart_text=(By.XPATH,"//p[text()='Your product has been added to cart.']")
    added_to_Cart_text=(By.ID,"cartModal")
    view_cart_button=(By.CSS_SELECTOR,"a[href='/view_cart']")
    continue_shopping_button=(By.XPATH,"//button[text()='Continue Shopping']")
    item_prices=(By.XPATH,"//div[@class='product-image-wrapper']//h2")
    product_image=(By.XPATH,"//div[@class='productinfo text-center']//img")
    product_price=(By.XPATH,"//div[@class='productinfo text-center']//h2")
    product_name=(By.XPATH,"//div[@class='productinfo text-center']//p")

    def __init__(self,driver:WebDriver):
        self.driver=driver

    def all_products_text_visibility(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.all_products_text)).is_displayed()

    def all_products_visibility(self):
        # products=self.driver.find_elements(*self.all_products)
        # count=len(products)-1
        # while count>=0:
        #     if not products[count].is_displayed():
        #         return False
        #     count-=1
        # return True
        products=WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(self.all_products))
        # for product in products:
        #     self.driver.execute_script(
        #         "arguments[0].scrollIntoView({block:'center'});",
        #         product
        #     )
        #
        #     if not product.is_displayed():
        #         return False
        # return True
        return len(products)>0

    def search_product(self,product_name):
        # self.driver.find_element(*self.search_product_bar).send_keys(product_name)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.search_product_bar)).send_keys(product_name)

    def search_invalid_product(self,product_name):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.search_product_bar)).send_keys(product_name)

    def click_search_button(self):
        self.driver.find_element(*self.search_product_button).click()

    def searched_product_visibility(self,product_name):
        products=self.driver.find_elements(*self.all_products)
        for i in products:
            if product_name.lower() not in i.text.lower():
                return False
        return True

    def invalid_search_product_visibility(self,product_name):
        products=self.driver.find_elements(*self.all_products)
        for i in products:
            if product_name.lower() in i.text.lower():
                return False
        return True

    def click_view_product_button(self,product_name):
        products=self.driver.find_elements(*self.all_products)
        view_product_selection=self.driver.find_elements(*self.view_product_button)
        for i in range(len(products)):
            if product_name.lower() in products[i].text.lower():
                safe_click=SafeClick(self.driver)
                safe_click.safe_click(view_product_selection[i])
                break

    def quantity_text_visibility(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.quantity_text)).is_displayed()

    def all_prices_visibility(self):
        # prices=self.driver.find_elements(*self.all_prices)
        # for i in prices:
        #     if not i.is_displayed():
        #         return False
        # return True
        prices=WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(self.all_prices))
        return len(prices)>0

    def select_category(self,category):
        categories=self.driver.find_elements(*self.all_categories)
        for i in categories:
            if i.text.lower()==category.lower():
                safe_click = SafeClick(self.driver)
                safe_click.safe_click(i)
                break

    def select_subcategory(self,sub_category):
        sub_categories=self.driver.find_elements(*self.all_categories)
        for i in sub_categories:
            if i.text.lower()==sub_category.lower():
                safe_click=SafeClick(self.driver)
                safe_click.safe_click(i)
                break

    def select_brandname(self,brandname):
        brandnames=self.driver.find_elements(*self.brand_names)
        for i in brandnames:
            if i.text.lower()==brandname.lower():
                safe_click = SafeClick(self.driver)
                safe_click.safe_click(i)
                break

    def category_selection_visibility(self):
        products=WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(self.all_products))
        return len(products)>0

    def add_to_cart_functionality(self,product_name):
        # products=self.driver.find_elements(*self.all_products)
        products=WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(self.all_products))
        for i in products:
            if product_name.lower() in i.text.lower():
                ActionChains(self.driver).move_to_element(i).perform()
                add_button=i.find_element(*self.add_to_cart_button)
                safe_click=SafeClick(self.driver)
                safe_click.safe_click(add_button)
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(self.added_to_Cart_text)
                )
                break

    def added_to_cart_text_visibility(self):
        # return self.driver.find_element(*self.added_to_Cart_text).is_displayed()
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.added_to_Cart_text)).is_displayed()

    def click_view_cart_button(self):
        safe_click=SafeClick(self.driver)
        view_cart_click=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.view_cart_button))
        safe_click.safe_click(view_cart_click)
        # safe_click.safe_click(self.driver.find_element(*self.view_cart_button))

    def view_cart_button_text_visibility(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.view_cart_button)).is_displayed()

    def click_continue_shopping_button(self):
        safe_click=SafeClick(self.driver)
        safe_click.safe_click(WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.continue_shopping_button)))

    def continue_shopping_button_text_visibility(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.continue_shopping_button)).is_displayed()

    def add_multiple_quantity_of_a_product(self,count,product_name):
        products=0
        while count>0:
            self.add_to_cart_functionality(product_name)
            self.click_continue_shopping_button()
            products+=1
            count-=1
        return products

    def get_item_prices(self,product_name):
        prices=0
        products=self.driver.find_elements(*self.all_products)
        for i in products:
            if i.text.lower()==product_name.lower():
                prices=int(i.find_element(*self.all_prices).text)
                break
        return prices

    def product_image_visibility(self):
        products=self.driver.find_elements(*self.all_products)
        for i in products:
            image=i.find_element(*self.product_image)
            if not image.is_displayed():
                return False
        return True

    def product_name_visibility(self):
        products=self.driver.find_elements(*self.all_products)
        for i in products:
            name=i.find_element(*self.product_name)
            if not name.is_displayed():
                return False
        return True

    def product_price_visibility(self):
        products=self.driver.find_elements(*self.all_products)
        for i in products:
            price=i.find_element(*self.product_price)
            if not price.is_displayed():
                return False
        return True

    def add_to_cart_hover(self,product_name):
        products=self.driver.find_elements(*self.all_products)
        for i in products:
            if product_name.lower() in i.text.lower():
                act=ActionChains(self.driver)
                act.move_to_element(i).move_to_element(i.find_element(*self.add_to_cart_button)).perform()
                # return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.added_to_Cart_text)).is_displayed()
                # self.driver.find_element(*self.added_to_Cart_text).is_displayed()

    def add_to_cart_visibility(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.add_to_cart_button)).is_displayed()






