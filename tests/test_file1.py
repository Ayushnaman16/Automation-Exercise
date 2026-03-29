from jinja2.filters import select_or_reject
from selenium import webdriver

from pages.HomePage import HomePage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.SignupPage import SignupPage
from pages.ContactUsPage import ContactUsPage
from pages.PaymentPage import PaymentPage
from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.base_test import Base_Test
from pages.TestCasesPage import TestCasesPage
import os
from utilities.Excel_Utility import readCellData,writeCellData,fillGreenColor,fillRedColor
from utilities.PassFailReporting import update_test_result
from utilities.CustomLogger import LogGen
from utilities.readProperties import ReadConfig

class TestFile1(Base_Test):

    file='D:\\Automation Excercise\\testdata\\AutomationExercise_60_Unique_TestCases.xlsx'
    sheet = 'AutomationExercise_TestCases'
    # row = 2
    col = 8

    user_data = ReadConfig.get_section('commonInfo1')
    user_data1 = ReadConfig.get_section('commonInfo2')
    product_data=ReadConfig.get_section('productInfo')
    card_data=ReadConfig.get_section('cardInfo')
    logger=LogGen.loggen()

    def test_AE_REG_001(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)

        self.logger.info('Clicking on the Login/Signup button in REG_001.')
        hp.click_login_signup_button()

        if lp.login_to_your_account_text_visibility():
            self.logger.info('Login to your account text is displayed.')
            update_test_result(self.file,self.sheet,2,self.col,'pass')
            assert True
        else:
            self.logger.error('Login text is not available - FAIL')
            self.driver.save_screenshot(os.curdir+'\\screenshots\\test_AE_REG_001.png')
            update_test_result(self.file,self.sheet,2,self.col,'fail')
            assert False

    def test_AE_REG_002(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)
        sp=SignupPage(self.driver)

        self.logger.info('Clicking on the Login/Signup button in REG_002.')
        hp.click_login_signup_button()

        self.logger.info('Entering the signup details.')
        # lp.enter_signup_details("hmm","hmm69@gmail.com")
        lp.enter_signup_details(
            self.user_data['user_name'],
            self.user_data['user_email']
        )
        lp.click_signup_button()

        self.logger.info('Account information text is displayed.')
        assert sp.account_information_text_visibility()==True
        # sp.click_title_button("mr")
        # sp.fill_all_the_fields("hmmm","hmmm","kumar","abc","Colony","Bangalore","Karnataka","Urban","112233","123456789")
        # sp.select_date("15","February","2016")
        # sp.select_country("India")
        sp.click_title_button(self.user_data['title'])

        sp.fill_all_the_fields(
            self.user_data['password'],
            self.user_data['first_name'],
            self.user_data['last_name'],
            self.user_data['company'],
            self.user_data['address'],
            self.user_data['address2'],
            self.user_data['state'],
            self.user_data['city'],
            self.user_data['zipcode'],
            self.user_data['mobile_number']
        )

        sp.select_date(
            self.user_data['day'],
            self.user_data['month'],
            self.user_data['year']
        )
        sp.select_newsletter()

        self.logger.info('Clicking on the create account button.')
        sp.click_create_account_button()


        if sp.account_created_text_visibility():
            self.logger.info('Account is created.')
            update_test_result(self.file,self.sheet,3,self.col,'pass')
            sp.click_continue_button()
            hp.click_delete_account_button()
            assert True
        else:
            self.logger.error('Account is not created.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_REG_002.png')
            update_test_result(self.file,self.sheet,3,self.col,'fail')
            sp.click_continue_button()
            hp.click_delete_account_button()
            assert False
        # sp.click_continue_button()
        # hp.click_delete_account_button()

    def test_AE_REG_003(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)

        self.logger.info('Clicking on the Login/Signup button in REG_003.')
        hp.click_login_signup_button()

        self.logger.info('Entering the signup details.')
        # lp.enter_signup_details("dummy","dummy69@gmail.com")
        lp.enter_signup_details(
            self.user_data1['user_name'],
            self.user_data1['user_email']
        )
        lp.click_signup_button()

        if lp.account_already_exists_text_visibility():
            update_test_result(self.file,self.sheet,4,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_REG_003.png')
            update_test_result(self.file,self.sheet,4,self.col,'fail')
            assert False

    def test_AE_REG_004(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)
        sp=SignupPage(self.driver)

        self.logger.info('Clicking on the Login/Signup Button in REG_004.')
        hp.click_login_signup_button()

        self.logger.info('Enter the SignUp details.')
        # lp.enter_signup_details("hmm","hmmm69@gmail.com")
        lp.enter_signup_details(
            self.user_data['user_name'],
            self.user_data['user_email1']
        )
        self.logger.info('Click on the Signup button in REG_004.')
        lp.click_signup_button()

        self.logger.info('Account information test is visible.')
        assert sp.account_information_text_visibility()==True
        # sp.click_title_button("mr")
        # sp.fill_all_the_fields("hmmm","hmmm","kumar","abc","Colony","Bangalore","Karnataka","Urban","112233","123456789")
        # sp.select_date("15","February","2016")
        # sp.select_country("India")
        sp.click_title_button(self.user_data['title'])

        sp.fill_all_the_fields(
            self.user_data['password'],
            self.user_data['first_name'],
            self.user_data['last_name'],
            self.user_data['company'],
            self.user_data['address'],
            self.user_data['address2'],
            self.user_data['state'],
            self.user_data['city'],
            self.user_data['zipcode'],
            self.user_data['mobile_number']
        )

        sp.select_date(
            self.user_data['day'],
            self.user_data['month'],
            self.user_data['year']
        )

        sp.select_country(
            self.user_data['country']
        )

        sp.select_newsletter()
        if sp.check_required_fields():
            self.logger.info('All the required fields are filled.')
            update_test_result(self.file,self.sheet,5,self.col,'pass')
            assert True
        else:
            self.logger.info('The required fields are not filled properly.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_REG_004.png')
            update_test_result(self.file,self.sheet,5,self.col,'fail')
            assert False

    def test_AE_REG_005(self):
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        sp = SignupPage(self.driver)

        self.logger.info('Clicking on the Login/Signup button in REG_005.')
        hp.click_login_signup_button()

        self.logger.info('Entering the signup details.')
        # lp.enter_signup_details("hmm", "hmmmm69@gmail.com")
        lp.enter_signup_details(
            self.user_data['user_name'],
            self.user_data['user_email2']
        )
        self.logger.info('Clicking on the signup button.')
        lp.click_signup_button()

        self.logger.info('Account information text is visible.')
        assert sp.account_information_text_visibility() == True
        # sp.click_title_button("mr")
        sp.click_title_button(self.user_data['title'])
        # sp.fill_all_the_fields("hmmm", "hmmm", "kumar", "abc", "Colony", "Bangalore", "Karnataka", "Urban", "112233",
        #                        "123456789")
        sp.fill_all_the_fields(
            self.user_data['password'],
            self.user_data['first_name'],
            self.user_data['last_name'],
            self.user_data['company'],
            self.user_data['address'],
            self.user_data['address2'],
            self.user_data['state'],
            self.user_data['city'],
            self.user_data['zipcode'],
            self.user_data['mobile_number']
        )
        if sp.check_password_hidden():
            self.logger.info('The password is hidden.')
            update_test_result(self.file, self.sheet, 6, self.col, 'pass')
            assert True
        else:
            self.logger.info('The password is not hidden.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_REG_005.png')
            update_test_result(self.file,self.sheet,6,self.col,'fail')
            assert False

    def test_AE_REG_006(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)
        sp=SignupPage(self.driver)

        self.logger.info('Clicking on the Login/Signup button in REG_006.')
        hp.click_login_signup_button()

        self.logger.info('Entering the signup details.')
        # lp.enter_signup_details("hmm", "hm69@gmail.com")
        lp.enter_signup_details(
            self.user_data['user_name'],
            self.user_data['user_email3']
        )
        self.logger.info('Clicking the signup button.')
        lp.click_signup_button()

        self.logger.info('Account information text visibility.')
        assert sp.account_information_text_visibility() == True
        # sp.click_title_button("mr")
        sp.click_title_button(self.user_data['title'])
        # sp.select_date("15","February","2016")
        sp.select_date(
            self.user_data['day'],
            self.user_data['month'],
            self.user_data['year']
        )
        # assert sp.assert_selected_date("15")
        # assert sp.assert_selected_month('February')
        # assert sp.assert_selected_year('2016')
        if sp.assert_selected_date_of_birth(self.user_data['day'],self.user_data['month'],self.user_data['year']):
            self.logger.info('The date of birth is selected correctly.')
            update_test_result(self.file,self.sheet,7,self.col,'pass')
            assert True
        else:
            self.logger.info('The date of birth is not selected correctly.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_REG_006.png')
            update_test_result(self.file, self.sheet, 7, self.col, 'fail')
            assert False

    def test_AE_REG_007(self):
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        sp = SignupPage(self.driver)

        self.logger.info('Clicking on the Login/signup button in REG_007.')
        hp.click_login_signup_button()

        self.logger.info('Entering the signup details.')
        # lp.enter_signup_details("hmm", "hm69@gmail.com")
        lp.enter_signup_details(
            self.user_data['user_name'],
            self.user_data['user_email']
        )
        self.logger.info('Clicking on the signup button.')
        lp.click_signup_button()

        if sp.account_information_text_visibility():
            self.logger.info('Account information text is visible.')
            update_test_result(self.file,self.sheet,8,self.col,'pass')
            assert True
        else:
            self.logger.info('Account information text is not visible.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_REG_007.png')
            update_test_result(self.file,self.sheet,8,self.col,'fail')
            assert False

    def test_AE_REG_008(self):
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        sp = SignupPage(self.driver)

        self.logger.info('Clicking on the Login/Signup button in REG_008.')
        hp.click_login_signup_button()

        self.logger.info('Entering the signup details.')
        # lp.enter_signup_details("hmm", "hm69@gmail.com")
        lp.enter_signup_details(
            self.user_data['user_name'],
            self.user_data['user_email']
        )
        self.logger.info('Clicking on the signup button.')
        lp.click_signup_button()

        sp.select_newsletter()

        self.logger.info('The newsletter is selected.')
        assert sp.is_newsletter_selected()==True

        assert sp.account_information_text_visibility() == True
        # sp.click_title_button("mr")
        # sp.fill_all_the_fields("hmmm", "hmmm", "kumar", "abc", "Colony", "Bangalore", "Karnataka", "Urban", "112233",
        #                        "123456789")
        # sp.select_date("15", "February", "2016")
        # sp.select_country("India")
        sp.click_title_button(self.user_data['title'])

        sp.fill_all_the_fields(
            self.user_data['password'],
            self.user_data['first_name'],
            self.user_data['last_name'],
            self.user_data['company'],
            self.user_data['address'],
            self.user_data['address2'],
            self.user_data['state'],
            self.user_data['city'],
            self.user_data['zipcode'],
            self.user_data['mobile_number']
        )

        sp.select_date(
            self.user_data['day'],
            self.user_data['month'],
            self.user_data['year']
        )

        sp.select_country(
            self.user_data['country']
        )
        sp.select_newsletter()
        sp.click_create_account_button()

        if sp.account_created_text_visibility():
            self.logger.info('Account is created successfully.')
            update_test_result(self.file,self.sheet,9,self.col,'pass')
            hp.click_home_button()
            hp.click_delete_account_button()
            assert True
        else:
            self.logger.info('Account is not created.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_REG_008.png')
            update_test_result(self.file, self.sheet, 9, self.col, 'fail')
            hp.click_home_button()
            hp.click_delete_account_button()
            assert False

    def test_AE_LOGIN_001(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)

        self.logger.info('Clicking on the Login/Signup button in LOGIN_001.')
        hp.click_login_signup_button()

        self.logger.info('Entering the login details.')
        # lp.enter_login_details(email="dummy69@gmail.com",password="dummy")
        lp.enter_login_details(email=self.user_data1['user_email'], password=self.user_data1['password'])
        self.logger.info('Clicking on the login button.')
        lp.click_login_button()

        if hp.is_logged_in_visible():
            self.logger.info('User is logged in.')
            update_test_result(self.file,self.sheet,10,self.col,'pass')
            assert True
        else:
            self.logger.info('User is not logged in.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_LOGIN_001.png')
            update_test_result(self.file,self.sheet,10,self.col,'fail')
            assert False

    def test_AE_LOGIN_002(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)

        self.logger.info('Clicking on the Login/Signup button in LOGIN_002.')
        hp.click_login_signup_button()

        self.logger.info('Entering the login details.')
        # lp.enter_login_details(email="dummy69@gmail.com",password="dumm")
        lp.enter_login_details(email=self.user_data1['user_email'], password=self.user_data1['password'])
        self.logger.info('Clicking on the Login button.')
        lp.click_login_button()

        if lp.wrong_email_password_text_visibility():
            self.logger.info('Invalid username/password is entered.')
            update_test_result(self.file,self.sheet,11,self.col,'pass')
            assert True
        else:
            self.logger.info('User has been logged in.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_LOGIN_002.png')
            update_test_result(self.file,self.sheet,11,self.col,'fail')
            assert False

    def test_AE_LOGIN_003(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)

        self.logger.info('Clicking on the Login/Signup button in LOGIN_003.')
        hp.click_login_signup_button()

        if lp.enter_login_details(email=self.user_data1['user_email']) or lp.enter_login_details(password=self.user_data1['password']):
            if lp.get_login_pass_field_filled_status():
                self.logger.info('Email/password field is empty is displayed.')
                update_test_result(self.file,self.sheet,12,self.col,'pass')
                assert True
            else:
                self.logger.info('Email/password field is not empty.')
                self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_LOGIN_003.png')
                update_test_result(self.file,self.sheet,12,self.col,'fail')
                assert False

    def test_AE_LOGIN_004(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)

        self.logger.info('Clicking on th Login/Signup button in LOGIN_004.')
        hp.click_login_signup_button()

        self.logger.info('Entering the login details.')
        # lp.enter_login_details(email='dummy69@gmail.com',password='dummy')
        lp.enter_login_details(email=self.user_data1['user_email'], password=self.user_data1['password'])
        self.logger.info('Clicking the login button.')
        lp.click_login_button()

        if hp.get_the_logged_in_name()==self.user_data1['user_name']:
            self.logger.info('The logged in name is displayed correctly.')
            update_test_result(self.file,self.sheet,13,self.col,'pass')
            assert True
        else:
            self.logger.info('The logged in name is not displayed.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_LOGIN_004.png')
            update_test_result(self.file,self.sheet,13,self.col,'fail')
            assert False

    def test_AE_LOGIN_005(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)

        self.logger.info('Clicking the Login/Signup button in LOGIN_005.')
        hp.click_login_signup_button()

        self.logger.info('Entering the login details.')
        # lp.enter_login_details(email='dummy69@gmail.com',password='dummy')
        lp.enter_login_details(email=self.user_data1['user_email'], password=self.user_data1['password'])
        self.logger.info('Clicking the login button.')
        lp.click_login_button()

        self.logger.info('Clicking the logout button.')
        hp.click_logout_button()

        if lp.login_to_your_account_text_visibility():
            self.logger.info('The user has been logged out.')
            update_test_result(self.file,self.sheet,14,self.col,'pass')
            assert True
        else:
            self.logger.info('The user session is still active.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_LOGIN_005.png')
            update_test_result(self.file,self.sheet,14,self.col,'fail')
            assert False

    def test_AE_LOGIN_006(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)

        self.logger.info('Clicking the Login/Signup button in LOGIN_006.')
        hp.click_login_signup_button()

        self.logger.info('Entering the login details.')
        # lp.enter_login_details(email='dummy69@gmail.com',password='dummy')
        lp.enter_login_details(email=self.user_data1['user_email'], password=self.user_data1['password'])
        self.logger.info('Clicking the login button.')
        lp.click_login_button()

        assert hp.is_logged_in_visible()==True

        self.logger.info('Refreshing the page.')
        hp.page_refresh()

        if hp.is_logged_in_visible():
            self.logger.info('The page is correctly visible after refresh.')
            update_test_result(self.file,self.sheet,15,self.col,'pass')
            assert True
        else:
            self.logger.info('The correct page is not displayed after the refresh.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_LOGIN_006.png')
            update_test_result(self.file,self.sheet,15,self.col,'fail')
            assert False

    def test_AE_PROD_001(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)
        pp=ProductsPage(self.driver)

        self.logger.info('Clicking the product button in PROD_001.')
        hp.click_product_button()

        if pp.all_products_text_visibility():
            self.logger.info('All the products text is displayed correctly.')
            update_test_result(self.file,self.sheet,16,self.col,'pass')
            assert True
        else:
            self.logger.info('All products text is not correctly visible.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_PROD_001.png')
            update_test_result(self.file,self.sheet,16,self.col,'fail')
            assert False

    def test_AE_PROD_002(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        self.logger.info('Clicking the product button in PROD_002.')
        hp.click_product_button()

        if pp.all_products_visibility():
            self.logger.info('All products are visible.')
            update_test_result(self.file,self.sheet,17,self.col,'pass')
            assert True
        else:
            self.logger.info('The products are not visible correctly.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_PROD_002.png')
            update_test_result(self.file,self.sheet,17,self.col,'fail')
            assert False

    def test_AE_PROD_003(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        self.logger.info('Clicking the product button in PROD_003.')
        hp.click_product_button()

        self.logger.info('Searching for product.')
        # pp.search_product('saree')
        pp.search_product(self.product_data['product'])
        self.logger.info('Clicking the search button.')
        pp.click_search_button()

        if pp.searched_product_visibility(self.product_data['product']):
            self.logger.info('The correct product is searched.')
            update_test_result(self.file,self.sheet,18,self.col,'pass')
            assert True
        else:
            self.logger.info('The product is not searched correctly.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_PROD_003.png')
            update_test_result(self.file,self.sheet,18,self.col,'fail')
            assert False

    def test_AE_PROD_004(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        self.logger.info('Clicking the product button in PROD_004.')
        hp.click_product_button()

        self.logger.info('Searching for an invalid product.')
        pp.search_invalid_product(self.product_data['product1'])
        self.logger.info('Clicking the search button.')
        pp.click_search_button()

        if pp.invalid_search_product_visibility(self.product_data['product1']):
            self.logger.info('The invalid product is not visible on the product page.')
            update_test_result(self.file,self.sheet,19,self.col,'pass')
            assert True
        else:
            self.logger.info('Th invalid product is visible on the products page.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_PROD_004.png')
            update_test_result(self.file,self.sheet,19,self.col,'fail')
            assert False

    def test_AE_PROD_005(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        self.logger.info('Clicking the product button in PROD_005.')
        hp.click_product_button()

        self.logger.info('Clicking the view product button.')
        pp.click_view_product_button(self.product_data['product2'])

        if pp.quantity_text_visibility():
            self.logger.info('The correct product is viewed.')
            update_test_result(self.file,self.sheet,20,self.col,'pass')
            assert True
        else:
            self.logger.info('The correct product is not viewed.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_PROD_005.png')
            update_test_result(self.file,self.sheet,20,self.col,'fail')
            assert False

    def test_AE_PROD_006(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        self.logger.info('Clicking the product button in PROD_006.')
        hp.click_product_button()

        if pp.all_prices_visibility():
            self.logger.info('All the prices are visible correctly.')
            update_test_result(self.file,self.sheet,21,self.col,'pass')
            assert True
        else:
            self.logger.info('The prices are not visible correctly.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_PROD_006.png')
            update_test_result(self.file,self.sheet,21,self.col,'fail')
            assert False

    def test_AE_PROD_007(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        self.logger.info('Clicking the product button in PROD_007.')
        hp.click_product_button()

        self.logger.info('Selecting the category.')
        pp.select_category(self.product_data['category'])
        self.logger.info('Selecting the sub-category.')
        pp.select_subcategory(self.product_data['subcategory'])
        self.logger.info('Selecting the brand name.')
        pp.select_brandname(self.product_data['brandname'])

        if pp.category_selection_visibility():
            self.logger.info('The correct products are searched according to the category.')
            update_test_result(self.file,self.sheet,22,self.col,'pass')
            assert True
        else:
            self.logger.info('The correct products are not displayed according to the category.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_PROD_007.png')
            update_test_result(self.file,self.sheet,22,self.col,'fail')
            assert False

    def test_AE_CART_001(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)
        cp=CartPage(self.driver)

        self.logger.info('Clicking the product button in CART_001.')
        hp.click_product_button()

        self.logger.info('Adding the product to the cart.')
        pp.add_to_cart_functionality(self.product_data['product3'])
        if pp.added_to_cart_text_visibility():
            self.logger.info('Added to cart text box is displayed.')
            update_test_result(self.file,self.sheet,23,self.col,'pass')
            assert True
        else:
            self.logger.info('Added to cart text box is not displayed.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CART_001.png')
            update_test_result(self.file,self.sheet,23,self.col,'fail')
            assert False

    def test_AE_CART_002(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)
        cp=CartPage(self.driver)

        self.logger.info('Clicking the product button in CART_002.')
        hp.click_product_button()

        self.logger.info('Adding the product to the cart.')
        pp.add_to_cart_functionality(self.product_data['product3'])
        self.logger.info('Added to cart test box is displayed.')
        assert pp.added_to_cart_text_visibility()==True
        self.logger.info('Clicking the view cart button.')
        pp.click_view_cart_button()
        # assert 'Men Tshirt' in cp.product_description_text()
        for i in cp.product_description_text():
            if self.product_data['product3'] in i:
                self.logger.info('The correct product is visible in the cart.')
                update_test_result(self.file,self.sheet,24,self.col,'pass')
                assert True
            else:
                self.logger.info('The correct product is not visible in the cart.')
                self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CART_002.png')
                update_test_result(self.file,self.sheet,24,self.col,'fail')
                assert False

    def test_AE_CART_003(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)
        cp=CartPage(self.driver)

        self.logger.info('Clicking the product button in CART_003.')
        hp.click_product_button()

        # pp.add_to_cart_functionality('Men Tshirt')
        # pp.click_continue_shopping_button()
        #
        # pp.add_to_cart_functionality('Men Tshirt')
        # pp.click_view_cart_button()

        self.logger.info('Adding multiple quantity of the same product.')
        cart_count=pp.add_multiple_quantity_of_a_product(self.product_data['count'],self.product_data['product3'])
        hp.click_cart_button()

        if int(cp.quantity_text_visibility())==cart_count:
            self.logger.info('Cart quantity is equal to the total times the product is added to the cart.')
            update_test_result(self.file,self.sheet,25,self.col,'pass')
            assert True
        else:
            self.logger.info('Cart quantity is not correct.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CART_003.png')
            update_test_result(self.file,self.sheet,25,self.col,'fail')
            assert False

    def test_AE_CART_004(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)
        cp=CartPage(self.driver)

        self.logger.info('Clicking the product button in CART_004.')
        hp.click_product_button()

        self.logger.info('Adding the product to the cart.')
        pp.add_to_cart_functionality(self.product_data['product3'])
        self.logger.info('Added to cart text box is visible.')
        assert pp.added_to_cart_text_visibility() == True
        self.logger.info('Clicking the continue to shopping button.')
        pp.click_continue_shopping_button()
        self.logger.info('Adding another product to the cart.')
        pp.add_to_cart_functionality(self.product_data['product4'])
        self.logger.info('Added to cart text box is visible.')
        assert pp.added_to_cart_text_visibility()==True

        self.logger.info('Clicking the view cart button.')
        pp.click_view_cart_button()

        # for i in cp.product_description_text():
        #     if 'Men Tshirt' in i:
        #         writeCellData(self.file, self.sheet, self.row + 1, self.col, "PASS")
        #         fillGreenColor(self.file, self.sheet, self.row + 1, self.col)
        #         assert True
        #
        #     if 'Sleeveless Dress' in i:
        #         writeCellData(self.file, self.sheet, self.row + 1, self.col, "PASS")
        #         fillGreenColor(self.file, self.sheet, self.row + 1, self.col)
        #         assert True
        self.logger.info('Checking the cart product description.')
        for i in cp.product_description_text():
            if self.product_data['product3'] in i:
                has_tshirt = True
            if self.product_data['product4'] in i:
                has_dress = True

        if has_tshirt and has_dress:
            self.logger.info('The correct product description is displayed.')
            update_test_result(self.file,self.sheet,26,self.col,'pass')
            assert True
        else:
            self.logger.info('The correct product description is not displayed.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CART_004.png')
            update_test_result(self.file,self.sheet,26,self.col,'fail')
            assert False

        # assert 'Men Tshirt' in cp.product_description_text()
        # assert 'Sleeveless Dress' in cp.product_description_text()

    def test_AE_CART_005(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)
        cp=CartPage(self.driver)

        self.logger.info('Clicking on the product button in CART_005.')
        hp.click_product_button()

        self.logger.info('Adding the product to the cart.')
        pp.add_to_cart_functionality(self.product_data['product3'])
        self.logger.info('Added to cart text is displayed.')
        assert pp.added_to_cart_text_visibility() == True

        self.logger.info('Clicking on the view cart button.')
        pp.click_view_cart_button()
        for i in cp.product_description_text():
            if self.product_data['product3'] in i:
                assert True
        # assert 'Men Tshirt' in cp.product_description_text()

        self.logger.info('Deleting the item from the cart.')
        cp.click_delete_item_button(self.product_data['product3'])
        if cp.cart_empty_text_visibility():
            self.logger.info('Cart is empty text is displayed.')
            update_test_result(self.file,self.sheet,27,self.col,'pass')
            assert True
        else:
            self.logger.info('Cart is not empty.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CART_005.png')
            update_test_result(self.file,self.sheet,27,self.col,'fail')
            assert False

    def test_AE_CART_006(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)
        cp=CartPage(self.driver)

        self.logger.info('Clicking on the product button in CART_006.')
        hp.click_product_button()

        self.logger.info('Adding multiple items to cart and storing the count value.')
        cart_count=pp.add_multiple_quantity_of_a_product(self.product_data['count'],self.product_data['product3'])
        # print(cart_count)
        total_cart_value = cart_count * pp.get_item_prices(self.product_data['product3'])
        # print(total_cart_value)
        self.logger.info('Clicking the cart button.')
        hp.click_cart_button()
        # print(cp.get_cart_total_value())
        for i in cp.get_cart_total_value():
            if total_cart_value==i:
                self.logger.info('Total cart value is correct.')
                update_test_result(self.file,self.sheet,28,self.col,'pass')
                assert True
            else:
                self.logger.info('Total cart value is not matching.')
                self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CART_006.png')
                update_test_result(self.file,self.sheet,28,self.col,'fail')
                assert False

    def test_AE_CHECK_001(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)
        pp=ProductsPage(self.driver)
        cp=CartPage(self.driver)
        chp=CheckoutPage(self.driver)

        self.logger.info('Clicking on the Login/Signup button in CHECK_001.')
        hp.click_login_signup_button()

        self.logger.info('Entering the login details.')
        lp.enter_login_details(email=self.user_data1['user_email'],password=self.user_data1['password'])
        self.logger.info('Clicking the login button.')
        lp.click_login_button()

        self.logger.info('Clicking on the product button.')
        hp.click_product_button()

        self.logger.info('Adding the product to the cart.')
        pp.add_to_cart_functionality(self.product_data['product3'])
        self.logger.info('Clicking on the view cart button.')
        pp.click_view_cart_button()

        assert cp.product_description_visibility()==True

        cp.click_proceed_to_checkout_button()

        if chp.review_order_text_visibility():
            self.logger.info('Review order page is displayed.')
            update_test_result(self.file,self.sheet,29,self.col,'pass')
            assert True
        else:
            self.logger.info('Rreview order page is not displayed.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CHECK_001.png')
            update_test_result(self.file, self.sheet,29, self.col, 'fail')
            assert False

    def test_AE_CHECK_002(self):
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        pp = ProductsPage(self.driver)
        cp = CartPage(self.driver)
        chp = CheckoutPage(self.driver)
        pap = PaymentPage(self.driver)

        self.logger.info('Clicking on the product button in CHECK_002.')
        hp.click_product_button()

        self.logger.info('Adding th product to the cart.')
        pp.add_to_cart_functionality(self.product_data['product3'])
        assert pp.added_to_cart_text_visibility() == True
        # pp.click_continue_shopping_button()
        self.logger.info('Clicking on the view cart button.')
        pp.click_view_cart_button()

        # hp.click_cart_button()
        self.logger.info('Clicking on the proceed to checkout button.')
        cp.click_proceed_to_checkout_button()

        if cp.register_login_text_visibility():
            self.logger.info('Register/Login text box is displayed.')
            update_test_result(self.file,self.sheet,30,self.col,'pass')
            assert True
        else:
            self.logger.info('Register/Login text box is not displayed.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CHECK_002.png')
            update_test_result(self.file, self.sheet, 30, self.col, 'fail')
            assert False

    def test_AE_CHECK_003(self):
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        pp = ProductsPage(self.driver)
        cp = CartPage(self.driver)
        chp = CheckoutPage(self.driver)
        pap = PaymentPage(self.driver)

        self.logger.info('Clicking on the login/signup button in CHECK_003.')
        hp.click_login_signup_button()

        self.logger.info('Entering the login details.')
        lp.enter_login_details(email=self.user_data1['user_email'], password=self.user_data1['password'])
        self.logger.info('Clicking the login button.')
        lp.click_login_button()

        self.logger.info('Clicking thr product button.')
        hp.click_product_button()

        self.logger.info('Adding the product to the cart.')
        pp.add_to_cart_functionality(self.product_data['product3'])
        assert pp.added_to_cart_text_visibility() == True
        # pp.click_continue_shopping_button()
        self.logger.info('Clicking the view cart button.')
        pp.click_view_cart_button()


        # hp.click_cart_button()
        self.logger.info('Clicking the proceed to checkout button.')
        cp.click_proceed_to_checkout_button()

        if chp.your_delivery_address_text_visibility():
            self.logger.info('Correct delivery address is displayed.')
            update_test_result(self.file, self.sheet, 31, self.col, 'pass')
            assert True
        else:
            self.logger.info('Delivery address is not displayed.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CHECK_003.png')
            update_test_result(self.file,self.sheet,31,self.col,'fail')
            assert False

    def test_AE_CHECK_004(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)
        pp=ProductsPage(self.driver)
        cp=CartPage(self.driver)
        chp=CheckoutPage(self.driver)

        self.logger.info('Clicking on the Login/signup button in CHECK_004.')
        hp.click_login_signup_button()

        self.logger.info('Entering the login details.')
        lp.enter_login_details(email=self.user_data1['user_email'],password=self.user_data1['password'])
        self.logger.info('Clicking the login button.')
        lp.click_login_button()

        self.logger.info('Click the product button.')
        hp.click_product_button()

        self.logger.info('Adding the product to the cart.')
        pp.add_to_cart_functionality(self.product_data['product3'])
        self.logger.info('Click the view cart button.')
        pp.click_view_cart_button()

        assert cp.product_description_visibility()==True

        self.logger.info('Click proceed to checkout button.')
        cp.click_proceed_to_checkout_button()

        if cp.get_cart_description_text(self.product_data['product3'])==chp.get_product_description_text(self.product_data['product3']):
            self.logger.info('Correct product information is displayed.')
            update_test_result(self.file,self.sheet,32,self.col,'pass')
            assert True
        else:
            self.logger.info('Product information is wrong.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CHECK_004.png')
            update_test_result(self.file,self.sheet,32,self.col,'fail')
            assert False

    def test_AE_CHECK_005(self):
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        pp = ProductsPage(self.driver)
        cp = CartPage(self.driver)
        chp = CheckoutPage(self.driver)
        pap = PaymentPage(self.driver)

        self.logger.info('Click on the Login/signup button in CHECK_005.')
        hp.click_login_signup_button()

        self.logger.info('Entering the login details.')
        lp.enter_login_details(email=self.user_data1['user_email'], password=self.user_data1['password'])
        self.logger.info('Clicking on the login button.')
        lp.click_login_button()

        self.logger.info('Clicking the product button.')
        hp.click_product_button()

        self.logger.info('Adding the product to the cart.')
        pp.add_to_cart_functionality(self.product_data['product3'])
        assert pp.added_to_cart_text_visibility() == True
        # pp.click_continue_shopping_button()
        self.logger.info('Clicking the view cart button.')
        pp.click_view_cart_button()

        # hp.click_cart_button()
        self.logger.info('Clicking the proceed to checkout button.')
        cp.click_proceed_to_checkout_button()

        self.logger.info('Clicking the place order button.')
        chp.click_place_order_button()

        self.logger.info('Entering the card details.')
        pap.enter_card_details(self.card_data['name'], self.card_data['cardnumber'], self.card_data['cvc'], self.card_data['month'], self.card_data['year'])
        self.logger.info('Clicking the pay button.')
        pap.click_pay_confirm_button()

        if pap.order_placed_text_visibility():
            self.logger.info('Order is placed successfully.')
            update_test_result(self.file,self.sheet,33,self.col,'pass')
            assert True
        else:
            self.logger.info('Order is not placed.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CHECK_005.png')
            update_test_result(self.file,self.sheet,33,self.col,'fail')
            assert False

    def test_AE_CONTACT_001(self):
        hp=HomePage(self.driver)
        cup=ContactUsPage(self.driver)

        self.logger.info('Clicking the contact us button in CONTACT_001.')
        hp.click_contact_us_button()

        if cup.contact_us_text_visibility():
            self.logger.info('Contact us text is displayed.')
            update_test_result(self.file,self.sheet,34,self.col,'pass')
            assert True
        else:
            self.logger.info('Contact us text is not displayed.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CONTACT_001.png')
            update_test_result(self.file,self.sheet,34,self.col,'fail')
            assert False

    def test_AE_CONTACT_002(self):
        hp=HomePage(self.driver)
        cup=ContactUsPage(self.driver)

        self.logger.info('Clicking the contact us button in CONTACT_002.')
        hp.click_contact_us_button()

        assert cup.contact_us_text_visibility()==True

        self.logger.info('Entering the contact us details.')
        cup.enter_contact_us_details(name=self.user_data1['user_name'],email=self.user_data1['user_email'],subject=self.user_data1['subject'],message=self.user_data1['message'])
        self.logger.info('Clicking the submit button.')
        cup.click_submit_button()
        self.logger.info('Handling the alerts.')
        cup.handling_alert()

        if cup.success_message_text_visibility():
            self.logger.info('Success message is displayed.')
            update_test_result(self.file,self.sheet,35,self.col,'pass')
            assert True
        else:
            self.logger.info('Success message is not displayed.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CONTACT_002.png')
            update_test_result(self.file,self.sheet,35,self.col,'fail')
            assert False

    def test_AE_CONTACT_003(self):
        hp=HomePage(self.driver)
        cup=ContactUsPage(self.driver)

        self.logger.info('Clicking the contact us button in CONTACT_003.')
        hp.click_contact_us_button()

        assert cup.contact_us_text_visibility()==True

        self.logger.info('Entering the contact us details.')
        cup.enter_contact_us_details(name=self.user_data1['user_name'],email=self.user_data1['user_email'],subject=self.user_data1['subject'],message=self.user_data1['message'])
        self.logger.info('Uploading the file.')
        cup.upload_file_functionality('D:\\Automation Excercise\\testdata\\AutomationExercise_60_Unique_TestCases.xlsx')
        self.logger.info('Clicking the submit button.')
        cup.click_submit_button()
        self.logger.info('Handling the alert.')
        cup.handling_alert()

        if cup.success_message_text_visibility():
            self.logger.info('Success message is displayed.')
            update_test_result(self.file,self.sheet,36,self.col,'pass')
            assert True
        else:
            self.logger.info('Success messafe is not displayed.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CONTACT_003.png')
            update_test_result(self.file,self.sheet,36,self.col,'fail')
            assert False

    def test_AE_SUB_001(self):
        hp=HomePage(self.driver)

        self.logger.info('Scrolling to the subscription field in SUB_001.')
        hp.scrolling_to_subscription_field()

        if hp.subscription_field_visibility():
            self.logger.info('Subscription field is displayed.')
            update_test_result(self.file,self.sheet,37,self.col,'pass')
            assert True
        else:
            self.logger.info('Subscription field is not displayed.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_SUB_001.png')
            update_test_result(self.file,self.sheet,37,self.col,'fail')
            assert False

    def test_AE_SUB_002(self):
        hp=HomePage(self.driver)

        self.logger.info('Scrolling to the subscription field in SUB_002.')
        hp.scrolling_to_subscription_field()

        self.logger.info('Entering the subscription email.')
        hp.enter_subscription_email(self.user_data1['user_email'])
        self.logger.info('Clicking on the subscribe button.')
        hp.click_subscribe_button()

        if hp.subscription_successful_message():
            self.logger.info('Subscription successful message is displayed.')
            update_test_result(self.file,self.sheet,38,self.col,'pass')
            assert True
        else:
            self.logger.info('Subscription successful message is not displayed.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_SUB_002.png')
            update_test_result(self.file,self.sheet,38,self.col,'fail')
            assert False

    def test_AE_SUB_003(self):
        hp=HomePage(self.driver)

        self.logger.info('Scrolling to the subscription field in SUB_003.')
        hp.scrolling_to_subscription_field()

        if hp.enter_invalid_subscription_email(self.user_data1['user_name']):
            self.logger.info('Entering invalid subscription email.')
            update_test_result(self.file,self.sheet,39,self.col,'pass')
            assert True
        else:
            self.logger.info('Valid email is entered.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_SUB_003.png')
            update_test_result(self.file,self.sheet,39,self.col,'fail')
            assert False

    def test_AE_ACC_001(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)
        sp=SignupPage(self.driver)

        self.logger.info('Clicking the Login/Signup button in ACC_001.')
        hp.click_login_signup_button()

        self.logger.info('Entering the signup details.')
        lp.enter_signup_details(self.user_data['user_name'], self.user_data['user_email'])
        self.logger.info('Clicking the signup button.')
        lp.click_signup_button()

        assert sp.account_information_text_visibility() == True
        self.logger.info('Entering the data into the fields.')
        # sp.click_title_button("mr")
        # sp.fill_all_the_fields("hmmm", "hmmm", "kumar", "abc", "Colony", "Bangalore", "Karnataka", "Urban", "112233",
        #                        "123456789")
        # sp.select_date("15", "February", "2016")
        # sp.select_country("India")
        sp.click_title_button(self.user_data['title'])

        sp.fill_all_the_fields(
            self.user_data['password'],
            self.user_data['first_name'],
            self.user_data['last_name'],
            self.user_data['company'],
            self.user_data['address'],
            self.user_data['address2'],
            self.user_data['state'],
            self.user_data['city'],
            self.user_data['zipcode'],
            self.user_data['mobile_number']
        )

        sp.select_date(
            self.user_data['day'],
            self.user_data['month'],
            self.user_data['year']
        )

        sp.select_country(
            self.user_data['country']
        )
        sp.select_newsletter()
        self.logger.info('Clicking the create account button.')
        sp.click_create_account_button()

        assert sp.account_created_text_visibility()==True

        self.logger.info('Clicking the home button.')
        hp.click_home_button()
        self.logger.info('Clicking the delete account button.')
        hp.click_delete_account_button()

        if hp.account_deleted_text_visibility():
            self.logger.info('Account is deleted successfully.')
            update_test_result(self.file,self.sheet,40,self.col,'pass')
            assert True
        else:
            self.logger.info('Account is not deleted.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_ACC_001.png')
            update_test_result(self.file, self.sheet, 40, self.col, 'fail')
            assert False

    def test_AE_ACC_002(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)
        sp=SignupPage(self.driver)

        self.logger.info('Clicking the Login/signup button in ACC_002.')
        hp.click_login_signup_button()

        self.logger.info('Entering the Signup details.')
        lp.enter_signup_details(self.user_data['user_name'], self.user_data['user_email'])
        self.logger.info('Clicking the signup button.')
        lp.click_signup_button()

        assert sp.account_information_text_visibility() == True
        self.logger.info('Entering the data in the required fields.')
        # sp.click_title_button("mr")
        # sp.fill_all_the_fields("hmmm", "hmmm", "kumar", "abc", "Colony", "Bangalore", "Karnataka", "Urban", "112233",
        #                        "123456789")
        # sp.select_date("15", "February", "2016")
        # sp.select_country("India")
        sp.click_title_button(self.user_data['title'])

        sp.fill_all_the_fields(
            self.user_data['password'],
            self.user_data['first_name'],
            self.user_data['last_name'],
            self.user_data['company'],
            self.user_data['address'],
            self.user_data['address2'],
            self.user_data['state'],
            self.user_data['city'],
            self.user_data['zipcode'],
            self.user_data['mobile_number']
        )

        sp.select_date(
            self.user_data['day'],
            self.user_data['month'],
            self.user_data['year']
        )

        sp.select_country(
            self.user_data['country']
        )
        sp.select_newsletter()
        self.logger.info('Clicking on the create account button.')
        sp.click_create_account_button()

        assert sp.account_created_text_visibility()==True

        self.logger.info('Clicking the home button.')
        hp.click_home_button()
        self.logger.info('Clicking the delete accout button.')
        hp.click_delete_account_button()

        assert hp.account_deleted_text_visibility()==True

        self.logger.info('Clicking the login/signup button.')
        hp.click_login_signup_button()

        self.logger.info('Enter the login details.')
        lp.enter_login_details(email=self.user_data['user_email'],password=self.user_data['password'])
        lp.click_login_button()

        if lp.wrong_email_password_text_visibility():
            self.logger.info('Wrong email/password text is displayed.')
            update_test_result(self.file,self.sheet,41,self.col,'pass')
            assert True
        else:
            self.logger.info('Valid email/password has been entered.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_ACC_002.png')
            update_test_result(self.file,self.sheet,41,self.col,'fail')
            assert False

    def test_AE_ACC_003(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)

        self.logger.info('Clicking the Login/Signup button in ACC_003.')
        hp.click_login_signup_button()

        self.logger.info('Entering the login details.')
        lp.enter_login_details(email=self.user_data['user_email3'],password=self.user_data['password'])
        self.logger.info('Clicking the login button.')
        lp.click_login_button()

        if lp.incorrect_email_text_visibility():
            self.logger.info('Incorrect email is being entered.')
            update_test_result(self.file,self.sheet,42,self.col,'pass')
            assert True
        else:
            self.logger.info('The email entered is valid.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_ACC_003.png')
            update_test_result(self.file,self.sheet,42,self.col,'fail')
            assert False

    def test_AE_NAV_001(self):
        hp=HomePage(self.driver)

        self.logger.info('Clicking the Home button in NAC_001;')
        hp.click_home_button()

        if hp.home_page_active_visibility():
            self.logger.info('Home page is active.')
            update_test_result(self.file,self.sheet,43,self.col,'pass')
            assert True
        else:
            self.logger.info('Home page is not active.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_NAV_001.png')
            update_test_result(self.file,self.sheet,43,self.col,'fail')
            assert False

    def test_AE_NAV_002(self):
        hp=HomePage(self.driver)
        tp=TestCasesPage(self.driver)

        self.logger.info('Clicking the test cases button in NAV_002.')
        hp.click_test_cases_button()

        if tp.list_of_test_cases_text_visibility():
            self.logger.info('The list of test cases are visible.')
            update_test_result(self.file,self.sheet,44,self.col,'pass')
            assert True
        else:
            self.logger.info('The list of test cases are not visible.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_NAV_002.png')
            update_test_result(self.file,self.sheet,44,self.col,'fail')
            assert False

    def test_AE_NAV_003(self):
        hp=HomePage(self.driver)

        self.logger.info('Scrolling to the subscription field in NAV_003.')
        hp.scrolling_to_subscription_field()

        self.logger.info('Clicking the scroll up button in NAV_003.')
        hp.click_scroll_up_button()

        if hp.home_page_active_visibility():
            self.logger.info('Home page is active.')
            update_test_result(self.file, self.sheet, 45, self.col, 'pass')
            assert True
        else:
            self.logger.info('Home page is not active.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_NAV_003.png')
            update_test_result(self.file, self.sheet, 45, self.col, 'fail')
            assert False

    def test_AE_UI_046(self):
        hp=HomePage(self.driver)

        self.logger.info('Page title is displayed in UI_046.')
        assert hp.page_title_visibility()==True
        if hp.page_title_clickable():
            self.logger.info('Page title is clickable.')
            update_test_result(self.file, self.sheet, 47, self.col, 'pass')
            assert True
        else:
            self.logger.info('Page title is not clickable.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_046.png')
            update_test_result(self.file, self.sheet, 47, self.col, 'fail')
            assert False

    def test_AE_UI_047(self):
        hp=HomePage(self.driver)

        self.logger.info('Top navigation menu is displayed in UI_047.')
        assert hp.top_navigation_menu_visibility()==True

        if hp.necessary_top_navigation_menu_visibility():
            self.logger.info('Important top navigation menu is visible.')
            update_test_result(self.file, self.sheet, 48, self.col, 'pass')
            assert True
        else:
            self.logger.info('The top navigation is not properly visible.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_047.png')
            update_test_result(self.file, self.sheet, 48, self.col, 'fail')
            assert False

    def test_AE_UI_048(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        self.logger.info('Clicking the home button in UI_048.')
        hp.click_home_button()

        if pp.all_products_text_visibility():
            self.logger.info('All products are being displayed.')
            update_test_result(self.file, self.sheet, 49, self.col, 'pass')
            assert True
        else:
            self.logger.info('All the products are not displayed properly.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_048.png')
            update_test_result(self.file, self.sheet, 49, self.col, 'fail')
            assert False

    def test_AE_UI_049(self):
        hp=HomePage(self.driver)
        cp=CartPage(self.driver)

        self.logger.info('Clicking the cart button in UI_049.')
        hp.click_cart_button()

        if cp.cart_empty_text_visibility():
            self.logger.info('The cart is empty.')
            update_test_result(self.file, self.sheet, 50, self.col, 'pass')
            assert True
        else:
            self.logger.info('The cart is not empty.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_049.png')
            update_test_result(self.file, self.sheet, 50, self.col, 'fail')
            assert False

    def test_AE_UI_050(self):
        hp=HomePage(self.driver)

        self.logger.info('Scrolling to the subscription field in UI_050.')
        hp.scrolling_to_subscription_field()

        if hp.footer_visibility():
            self.logger.info('The footer is correctly visible.')
            update_test_result(self.file, self.sheet, 51, self.col, 'pass')
            assert True
        else:
            self.logger.info('The footer is not visible.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_050.png')
            update_test_result(self.file, self.sheet, 51, self.col, 'fail')
            assert False

    def test_AE_UI_051(self):
        hp=HomePage(self.driver)

        self.logger.info('Scrolling to the subscription field in UI_051.')
        hp.scrolling_to_subscription_field()

        if hp.subscription_email_visibility():
            self.logger.info('Subscription email is visible.')
            update_test_result(self.file, self.sheet, 52, self.col, 'pass')
            assert True
        else:
            self.logger.info('Subscription email is not visible.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_051.png')
            update_test_result(self.file, self.sheet, 52, self.col, 'fail')
            assert False

    def test_AE_UI_052(self):
        hp=HomePage(self.driver)

        self.logger.info('Scrolling to the recommended items in UI_052.')
        hp.scrolling_to_recommended_items()

        if hp.recommended_items_visibility():
            self.logger.info('Recommended items is displayed.')
            update_test_result(self.file, self.sheet, 53, self.col, 'pass')
            assert True
        else:
            self.logger.info('Recommended items is not displayed.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_052.png')
            update_test_result(self.file, self.sheet, 53, self.col, 'fail')
            assert False

    def test_AE_UI_053(self):
        hp=HomePage(self.driver)

        self.logger.info('Scrolling to the recommended items in UI_053.')
        hp.scrolling_to_recommended_items()

        if hp.category_text_visibility():
            self.logger.info('Category is visible.')
            update_test_result(self.file, self.sheet, 54, self.col, 'pass')
            assert True
        else:
            self.logger.info('Category is not visible.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_053.png')
            update_test_result(self.file, self.sheet, 54, self.col, 'fail')
            assert False

    def test_AE_UI_054(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        self.logger.info('Selecting the category in UI_054.')
        pp.select_category(self.product_data['category1'])
        self.logger.info('Selecting the sub category.')
        pp.select_subcategory(self.product_data['subcategory1'])

        if pp.category_selection_visibility():
            self.logger.info('The category is correctly visible.')
            update_test_result(self.file, self.sheet, 55, self.col, 'pass')
            assert True
        else:
            self.logger.info('The category is not visible.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_054.png')
            update_test_result(self.file, self.sheet, 55, self.col, 'fail')
            assert False

    def test_AE_UI_055(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        self.logger.info('Product name,price and image is displayed in UI_055.')
        update_test_result(self.file, self.sheet, 56, self.col, 'pass')
        assert pp.product_name_visibility()==True
        assert pp.product_price_visibility()==True
        assert pp.product_image_visibility()==True

    def test_AE_UI_056(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        self.logger.info('Clicking the product button in UI_056.')
        hp.click_product_button()

        self.logger.info('Clicking the view product button.')
        pp.click_view_product_button(self.product_data['product3'])

        if pp.quantity_text_visibility():
            self.logger.info('Quantity is visible.')
            update_test_result(self.file, self.sheet, 57, self.col, 'pass')
            assert True
        else:
            self.logger.info('Product is not loaded completely.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_056.png')
            update_test_result(self.file, self.sheet, 57, self.col, 'fail')
            assert False

    def test_AE_UI_057(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        self.logger.info('Clicking the product button in UI_057.')
        hp.click_product_button()

        self.logger.info('Hovering to add to cart.')
        pp.add_to_cart_hover(self.product_data['product3'])

        if pp.add_to_cart_visibility():
            self.logger.info('Add to cart is displayed.')
            update_test_result(self.file, self.sheet, 58, self.col, 'pass')
            assert True
        else:
            self.logger.info('Add to cart is not displayed.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_057.png')
            update_test_result(self.file, self.sheet, 58, self.col, 'fail')
            assert False

    def test_AE_UI_058(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        self.logger.info('Clicking the product button in UI_058.')
        hp.click_product_button()

        self.logger.info('Adding the product to the cart.')
        pp.add_to_cart_functionality(self.product_data['product3'])

        update_test_result(self.file, self.sheet, 59, self.col, 'pass')
        assert pp.view_cart_button_text_visibility()==True
        assert pp.continue_shopping_button_text_visibility()==True

    def test_AE_UI_059(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        self.logger.info('Clicking the product button in UI_059.')
        hp.click_product_button()

        self.logger.info('Adding the product to the cart.')
        pp.add_to_cart_functionality(self.product_data['product3'])

        self.logger.info('Clicking the continue to shopping button.')
        pp.click_continue_shopping_button()

        if pp.all_products_text_visibility():
            self.logger.info('All products are displayed.')
            update_test_result(self.file, self.sheet, 60, self.col, 'pass')
            assert True
        else:
            self.logger.info('All products are not displayed.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_059.png')
            update_test_result(self.file, self.sheet, 60, self.col, 'fail')
            assert False

    def test_AE_UI_060(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)
        cp=CartPage(self.driver)

        self.logger.info('Clicking the product button in UI_060.')
        hp.click_product_button()

        self.logger.info('Adding the product to the cart.')
        pp.add_to_cart_functionality(self.product_data['product3'])

        self.logger.info('Clicking the view cart button.')
        pp.click_view_cart_button()

        if cp.product_description_visibility():
            self.logger.info('Product description is displayed correctly.')
            update_test_result(self.file, self.sheet, 61, self.col, 'pass')
            assert True
        else:
            self.logger.info('Product description is not displayed correctly.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_060.png')
            update_test_result(self.file, self.sheet, 61, self.col, 'fail')
            assert False













