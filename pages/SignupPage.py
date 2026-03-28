from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class SignupPage:

    mr_button=(By.CSS_SELECTOR,"input[value='Mr']")
    mrs_button=(By.CSS_SELECTOR,"input[value='Mrs']")
    password=(By.CSS_SELECTOR,"input#password")
    create_account_button=(By.CSS_SELECTOR,"button[data-qa='create-account']")
    first_name=(By.CSS_SELECTOR,"input[data-qa='first_name']")
    last_name=(By.CSS_SELECTOR,"input[data-qa='last_name']")
    company=(By.CSS_SELECTOR,"input[data-qa='company']")
    address=(By.CSS_SELECTOR,"input[data-qa='address']")
    address2=(By.CSS_SELECTOR,"input[data-qa='address2']")
    state=(By.CSS_SELECTOR,"input[data-qa='state']")
    city=(By.CSS_SELECTOR,"input[data-qa='city']")
    zipcode=(By.CSS_SELECTOR,"input[data-qa='zipcode']")
    mobile_number=(By.CSS_SELECTOR,"input[data-qa='mobile_number']")
    country=(By.CSS_SELECTOR,"select[data-qa='country']")
    day=(By.CSS_SELECTOR,"select[data-qa='days']")
    months=(By.CSS_SELECTOR,"select[data-qa='months']")
    year=(By.CSS_SELECTOR,"select[data-qa='years']")
    newsletter=(By.CSS_SELECTOR,"input[name='newsletter']")
    optin=(By.CSS_SELECTOR,"input[name='optin']")
    account_information_text=(By.XPATH,"//b[text()='Enter Account Information']")
    account_created_text=(By.XPATH,"//b[text()='Account Created!']")
    continue_button=(By.CSS_SELECTOR,"a[data-qa='continue-button']")
    required_fields=(By.CSS_SELECTOR,".required.form-group")

    def __init__(self,driver:WebDriver):
        self.driver=driver

    def click_title_button(self,title):
        if title=='mr' or title=='Mr' or title=='MR':
            self.driver.find_element(*self.mr_button).click()
        elif title=="mrs" or title=='Mrs' or title=='MRS':
            self.driver.find_element(*self.mrs_button).click()

    def fill_all_the_fields(self,password,first_name,last_name,company,address,address2,state,city,zipcode,mobile_number):
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.company).send_keys(company)
        self.driver.find_element(*self.address).send_keys(address)
        self.driver.find_element(*self.address2).send_keys(address2)
        self.driver.find_element(*self.state).send_keys(state)
        self.driver.find_element(*self.city).send_keys(city)
        self.driver.find_element(*self.zipcode).send_keys(zipcode)
        self.driver.find_element(*self.mobile_number).send_keys(mobile_number)
    #
    # def fill_all_the_fields(self, password, **kwargs):
    #
    #     self.driver.find_element(*self.password).send_keys(password)
    #
    #     fields = {
    #         "first_name": self.first_name,
    #         "last_name": self.last_name,
    #         "company": self.company,
    #         "address": self.address,
    #         "address2": self.address2,
    #         "state": self.state,
    #         "city": self.city,
    #         "zipcode": self.zipcode,
    #         "mobile_number": self.mobile_number
    #     }
    #
    #     for key, value in kwargs.items():
    #         if key in fields:
    #             self.driver.find_element(*fields[key]).send_keys(value)

    def select_date(self,day,month,year):
        day_selection=Select(self.driver.find_element(*self.day))
        day_selection.select_by_value(day)
        month_selection=Select(self.driver.find_element(*self.months))
        month_selection.select_by_visible_text(month)
        year_selection=Select(self.driver.find_element(*self.year))
        year_selection.select_by_value(year)

        # assert day_selection.first_selected_option.get_attribute("value") == day
        # assert month_selection.first_selected_option.text == month
        # assert year_selection.first_selected_option.get_attribute("value") == year

    def select_newsletter(self):
        # self.driver.find_element(*self.newsletter).click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.newsletter)).click()

    def select_optin(self):
        self.driver.find_element(*self.optin).click()

    def click_create_account_button(self):
        wait=WebDriverWait(self.driver,10)
        wait.until(EC.element_to_be_clickable(self.create_account_button)).click()
        # self.driver.find_element(*self.create_account_button).click()

    def account_information_text_visibility(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.account_information_text)).is_displayed()
        # wait=WebDriverWait(self.driver,10)
        # return wait.until(EC.presence_of_element_located(self.account_information_text)).is_displayed()

    def account_created_text_visibility(self):
        wait=WebDriverWait(self.driver,10)
        return wait.until(EC.presence_of_element_located(self.account_created_text)).is_displayed()

    def click_continue_button(self):
        self.driver.find_element(*self.continue_button).click()

    def select_country(self,country):
        country_selection=Select(self.driver.find_element(*self.country))
        country_selection.select_by_value(country)

    def check_required_fields(self):
        fields=self.driver.find_elements(*self.required_fields)
        for i in fields:
            field=i.find_element(By.CSS_SELECTOR,"input,select,textarea")
            if field.get_attribute("value")=="":
                return False
        return True

    def check_password_hidden(self):
        password_field = self.driver.find_element(*self.password)
        return password_field.get_attribute("type") == "password"

    def assert_selected_date_of_birth(self, day, month, year):
        day_dropdown = Select(self.driver.find_element(*self.day))
        month_dropdown = Select(self.driver.find_element(*self.months))
        year_dropdown = Select(self.driver.find_element(*self.year))
        return day_dropdown.first_selected_option.get_attribute("value") == day and month_dropdown.first_selected_option.text == month and year_dropdown.first_selected_option.get_attribute("value") == year

    # def assert_selected_month(self,month):
    #     month_dropdown = Select(self.driver.find_element(*self.months))
    #     return month_dropdown.first_selected_option.text == month
    #
    # def assert_selected_year(self,year):
    #     year_dropdown = Select(self.driver.find_element(*self.year))
    #     return year_dropdown.first_selected_option.get_attribute("value") == year

    def is_newsletter_selected(self):
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.newsletter)
        )
        return checkbox.is_selected()
