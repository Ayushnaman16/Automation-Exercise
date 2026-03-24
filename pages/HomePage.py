from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver

class HomePage:

    '''
    sample email-dummy69@gmail.com
    sample username-dummy
    sample password-dummy
    '''

    login_signup_button=(By.CSS_SELECTOR,"a[href='/login']")
    home_button=(By.XPATH,"//a[text()=' Home']")
    home_page_active_status=(By.CSS_SELECTOR,"a[style='color: orange;']")
    products_button=(By.CSS_SELECTOR,"a[href='/products']")
    cart_button=(By.XPATH,"//a[text()=' Cart']")
    page_title_image=(By.CSS_SELECTOR,"img[alt='Website for automation practice']")
    logged_in_as_button=(By.XPATH,"//a[text()=' Logged in as ']")
    logged_in_as_name=(By.XPATH,"//a[text()=' Logged in as ']/b")
    logout_button=(By.CSS_SELECTOR,"a[href='/logout']")
    delete_account_button=(By.CSS_SELECTOR,"a[href='/delete_account']")
    account_deleted_text=(By.XPATH,"//b[text()='Account Deleted!']")
    continue_button=(By.CSS_SELECTOR,"a[data-qa='continue-button']")
    added_text=(By.CSS_SELECTOR,"h4[class='modal-title w-100']")
    view_cart_button=(By.XPATH,"//u[text()='View Cart']")
    continue_shopping_button=(By.CSS_SELECTOR,"button[data-dismiss='modal']")
    ad_box=(By.CSS_SELECTOR,"div#ad_position_box")
    ad_box_close=(By.CSS_SELECTOR,"svg[viewBox='0 0 48 48']")
    contact_us_button=(By.CSS_SELECTOR,"a[href='/contact_us']")
    subscription_field=(By.CSS_SELECTOR,"div.single-widget")
    subscription_email=(By.CSS_SELECTOR,"input#susbscribe_email")
    subscribe_button=(By.CSS_SELECTOR,"button#subscribe")
    subscribe_success_message=(By.CSS_SELECTOR,"div.alert-success.alert")
    test_cases_button=(By.XPATH,"//a[text()=' Test Cases']")
    scroll_up_button=(By.CSS_SELECTOR,"a#scrollUp")
    top_navigation_menu=(By.CSS_SELECTOR,"ul.nav.navbar-nav")
    footer=(By.XPATH,"//div[@class='footer-widget']")
    recommended_items=(By.XPATH,"//h2[text()='Features Items']")
    category_text=(By.XPATH,"//h2[text()='Category']")

    def __init__(self,driver:WebDriver):
        self.driver=driver

    def click_test_cases_button(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.test_cases_button)).click()

    def click_login_signup_button(self):
        self.driver.find_element(*self.login_signup_button).click()

    def click_home_button(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.home_button)).click()

    def page_title_visibility(self):
        return self.driver.find_element(*self.page_title_image).is_displayed()

    def page_title_clickable(self):
        return self.driver.find_element(*self.page_title_image).is_enabled()

    def click_product_button(self):
        # self.driver.find_element(*self.products_button).click()
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.products_button)).click()

    def click_cart_button(self):
        self.driver.find_element(*self.cart_button).click()

    def click_view_cart_button(self):
        self.driver.find_element(*self.view_cart_button).click()

    def click_continue_shopping_button(self):
        self.driver.find_element(*self.continue_shopping_button).click()

    def click_continue_button(self):
        self.driver.find_element(*self.continue_button).click()

    def account_deleted_text_visibility(self):
        # return self.driver.find_element(*self.account_deleted_text).is_displayed()
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.account_deleted_text)).is_displayed()

    def click_delete_account_button(self):
        # self.driver.find_element(*self.delete_account_button).click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.delete_account_button)).click()

    def click_logout_button(self):
        # logout_button=self.driver.find_element(*self.logout_button)
        # self.driver.find_element(*self.logout_button).click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.logout_button)).click()

    def added_to_cart_text_visibility(self):
        return self.driver.find_element(*self.added_text).is_displayed()

    # def account_deletion(self):
    #     # self.driver.find_element(*self.home_button)
    #     self.click_delete_account_button()

    def is_logged_in_visible(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.logged_in_as_button)).is_displayed()

    def get_the_logged_in_name(self):
        # username=self.driver.find_element(*self.logged_in_as_name)
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.logged_in_as_name)).text
        # return self.driver.find_element(*self.logged_in_as_name).text

    def page_refresh(self):
        self.driver.refresh()

    def click_contact_us_button(self):
        # self.driver.find_element(*self.contact_us_button).click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.contact_us_button)).click()

    def scrolling_to_subscription_field(self):
        flag=self.driver.find_element(*self.subscription_field)
        self.driver.execute_script("arguments[0].scrollIntoView();",flag)

    def subscription_field_visibility(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.subscription_field)).is_displayed()

    def enter_subscription_email(self,email):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.subscription_email)).send_keys(email)

    def click_subscribe_button(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.subscribe_button)).click()

    def subscription_successful_message(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.subscribe_success_message)).is_displayed()

    def enter_invalid_subscription_email(self,email):
        email_details=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.subscription_email))
        email_details.send_keys(email)

        message = self.driver.execute_script(
            "return arguments[0].validationMessage;",
            email_details
        )
        return "Please include an '@' in the email address" in message

    def home_page_active_visibility(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.home_page_active_status)).is_displayed()

    def click_scroll_up_button(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.scroll_up_button)).click()

    def get_top_navigation_menu_text(self):
        return self.driver.find_element(*self.top_navigation_menu).text

    def top_navigation_menu_visibility(self):
        return self.driver.find_element(*self.top_navigation_menu).is_displayed()

    def necessary_top_navigation_menu_visibility(self):
        menu_name_list=['Home','Products','Cart','Signup / Login']
        text=self.get_top_navigation_menu_text()
        for i in menu_name_list:
            if i.lower() not in text.lower():
                return False
        return True
        # return 'Home' and 'Products' and 'Cart' and 'Signup/Login' in text

    def footer_visibility(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.footer)).is_displayed()

    def subscription_email_visibility(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.subscription_email)).is_displayed()

    def scrolling_to_recommended_items(self):
        flag=self.driver.find_element(*self.recommended_items)
        self.driver.execute_script('arguments[0].scrollIntoView();',flag)

    def recommended_items_visibility(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.recommended_items)).is_displayed()

    def category_text_visibility(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.category_text)).is_displayed()




