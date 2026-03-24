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

class TestFile1(Base_Test):

    file='D:\\Automation Excercise\\testdata\\AutomationExercise_60_Unique_TestCases.xlsx'
    sheet = 'AutomationExercise_TestCases'
    row = 2
    col = 8

    logger=LogGen.loggen()

    def test_AE_REG_001(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)

        self.logger.info('Clicking on the Login/Signup button.')
        hp.click_login_signup_button()

        if lp.login_to_your_account_text_visibility():
            self.logger.info('Login to your account text is displayed.')
            update_test_result(self.file,self.sheet,self.row,self.col,'pass')
            assert True
        else:
            self.logger.error('Login text is not available - FAIL')
            self.driver.save_screenshot(os.curdir+'\\screenshots\\test_AE_REG_001.png')
            update_test_result(self.file,self.sheet,self.row,self.col,'fail')
            assert False

    def test_AE_REG_002(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)
        sp=SignupPage(self.driver)

        self.logger.info('Clicking on the Login/Signup button.')
        hp.click_login_signup_button()

        self.logger.info('Entering the signup details.')
        lp.enter_signup_details("hmm","hmm69@gmail.com")
        lp.click_signup_button()

        self.logger.info('Account information text is displayed.')
        assert sp.account_information_text_visibility()==True
        sp.click_title_button("mr")
        sp.fill_all_the_fields("hmmm","hmmm","kumar","abc","Colony","Bangalore","Karnataka","Urban","112233","123456789")
        sp.select_date("15","February","2016")
        sp.select_country("India")
        sp.select_newsletter()

        self.logger.info('Clicking on the create account button.')
        sp.click_create_account_button()


        if sp.account_created_text_visibility():
            self.logger.info('Account is created.')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            sp.click_continue_button()
            hp.click_delete_account_button()
            assert True
        else:
            self.logger.error('Account is not created.')
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_REG_002.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            sp.click_continue_button()
            hp.click_delete_account_button()
            assert False
        # sp.click_continue_button()
        # hp.click_delete_account_button()

    def test_AE_REG_003(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)

        self.logger.info('Clicking on the create account button.')
        hp.click_login_signup_button()

        self.logger.info('Entering the signup details.')
        lp.enter_signup_details("dummy","dummy69@gmail.com")
        lp.click_signup_button()

        if lp.account_already_exists_text_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_REG_003.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_REG_004(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)
        sp=SignupPage(self.driver)

        hp.click_login_signup_button()

        lp.enter_signup_details("hmm","hmmm69@gmail.com")
        lp.click_signup_button()

        assert sp.account_information_text_visibility()==True
        sp.click_title_button("mr")
        sp.fill_all_the_fields("hmmm","hmmm","kumar","abc","Colony","Bangalore","Karnataka","Urban","112233","123456789")
        sp.select_date("15","February","2016")
        sp.select_country("India")
        sp.select_newsletter()
        if sp.check_required_fields():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_REG_004.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_REG_005(self):
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        sp = SignupPage(self.driver)

        hp.click_login_signup_button()

        lp.enter_signup_details("hmm", "hmmmm69@gmail.com")
        lp.click_signup_button()

        assert sp.account_information_text_visibility() == True
        sp.click_title_button("mr")
        sp.fill_all_the_fields("hmmm", "hmmm", "kumar", "abc", "Colony", "Bangalore", "Karnataka", "Urban", "112233",
                               "123456789")
        if sp.check_password_hidden():
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_REG_005.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_REG_006(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)
        sp=SignupPage(self.driver)

        hp.click_login_signup_button()

        lp.enter_signup_details("hmm", "hm69@gmail.com")
        lp.click_signup_button()

        assert sp.account_information_text_visibility() == True
        sp.click_title_button("mr")
        sp.select_date("15","February","2016")

        # assert sp.assert_selected_date("15")
        # assert sp.assert_selected_month('February')
        # assert sp.assert_selected_year('2016')
        if sp.assert_selected_date_of_birth('15','February','2016'):
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_REG_006.png')
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'fail')
            assert False

    def test_AE_REG_007(self):
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        sp = SignupPage(self.driver)

        hp.click_login_signup_button()

        lp.enter_signup_details("hmm", "hm69@gmail.com")
        lp.click_signup_button()

        if sp.account_information_text_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_REG_007.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_REG_008(self):
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        sp = SignupPage(self.driver)

        hp.click_login_signup_button()

        lp.enter_signup_details("hmm", "hm69@gmail.com")
        lp.click_signup_button()

        sp.select_newsletter()

        assert sp.is_newsletter_selected()==True

        assert sp.account_information_text_visibility() == True
        sp.click_title_button("mr")
        sp.fill_all_the_fields("hmmm", "hmmm", "kumar", "abc", "Colony", "Bangalore", "Karnataka", "Urban", "112233",
                               "123456789")
        sp.select_date("15", "February", "2016")
        sp.select_country("India")
        sp.select_newsletter()
        sp.click_create_account_button()

        if sp.account_created_text_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_REG_008.png')
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'fail')
            assert False
        hp.click_home_button()
        hp.click_delete_account_button()

    def test_AE_LOGIN_001(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)

        hp.click_login_signup_button()

        lp.enter_login_details(email="dummy69@gmail.com",password="dummy")
        lp.click_login_button()

        if hp.is_logged_in_visible():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_LOGIN_001.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_LOGIN_002(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)

        hp.click_login_signup_button()

        lp.enter_login_details(email="dummy69@gmail.com",password="dumm")
        lp.click_login_button()

        if lp.wrong_email_password_text_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_LOGIN_002.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_LOGIN_003(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)

        hp.click_login_signup_button()

        if lp.enter_login_details(email='dummy69@gmail.com') or lp.enter_login_details(password='dummy'):
            if lp.get_login_pass_field_filled_status():
                update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
                assert True
            else:
                self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_LOGIN_003.png')
                update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
                assert False

    def test_AE_LOGIN_004(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)

        hp.click_login_signup_button()

        lp.enter_login_details(email='dummy69@gmail.com',password='dummy')
        lp.click_login_button()

        if hp.get_the_logged_in_name()=='dummy':
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_LOGIN_004.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_LOGIN_005(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)

        hp.click_login_signup_button()

        lp.enter_login_details(email='dummy69@gmail.com',password='dummy')
        lp.click_login_button()

        hp.click_logout_button()

        if lp.login_to_your_account_text_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_LOGIN_005.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_LOGIN_006(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)

        hp.click_login_signup_button()

        lp.enter_login_details(email='dummy69@gmail.com',password='dummy')
        lp.click_login_button()

        assert hp.is_logged_in_visible()==True
        hp.page_refresh()
        if hp.is_logged_in_visible():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_LOGIN_006.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_PROD_001(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)
        pp=ProductsPage(self.driver)

        hp.click_product_button()

        if pp.all_products_text_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_PROD_001.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_PROD_002(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        hp.click_product_button()

        if pp.all_products_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_PROD_002.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_PROD_003(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        hp.click_product_button()

        pp.search_product('saree')
        pp.click_search_button()

        if pp.searched_product_visibility('saree'):
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_PROD_003.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_PROD_004(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        hp.click_product_button()

        pp.search_invalid_product('pyjama')
        pp.click_search_button()

        if pp.invalid_search_product_visibility('pyjama'):
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_PROD_004.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_PROD_005(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        hp.click_product_button()

        pp.click_view_product_button('Stylish Dress')

        if pp.quantity_text_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_PROD_005.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_PROD_006(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        hp.click_product_button()

        if pp.all_prices_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_PROD_006.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_PROD_007(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        hp.click_product_button()

        pp.select_category('men')
        pp.select_subcategory('tshirts')
        pp.select_brandname('polo')

        if pp.category_selection_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_PROD_007.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_CART_001(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)
        cp=CartPage(self.driver)

        hp.click_product_button()

        pp.add_to_cart_functionality('Men Tshirt')
        if pp.added_to_cart_text_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CART_001.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_CART_002(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)
        cp=CartPage(self.driver)

        hp.click_product_button()

        pp.add_to_cart_functionality('Men Tshirt')
        assert pp.added_to_cart_text_visibility()==True

        pp.click_view_cart_button()
        # assert 'Men Tshirt' in cp.product_description_text()
        for i in cp.product_description_text():
            if 'Men Tshirt' in i:
                update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
                assert True
            else:
                self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CART_002.png')
                update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
                assert False

    def test_AE_CART_003(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)
        cp=CartPage(self.driver)

        hp.click_product_button()

        # pp.add_to_cart_functionality('Men Tshirt')
        # pp.click_continue_shopping_button()
        #
        # pp.add_to_cart_functionality('Men Tshirt')
        # pp.click_view_cart_button()

        cart_count=pp.add_multiple_quantity_of_a_product(3,'Men Tshirt')
        hp.click_cart_button()

        if int(cp.quantity_text_visibility())==cart_count:
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CART_003.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_CART_004(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)
        cp=CartPage(self.driver)

        hp.click_product_button()

        pp.add_to_cart_functionality('Men Tshirt')
        assert pp.added_to_cart_text_visibility() == True

        pp.click_continue_shopping_button()

        pp.add_to_cart_functionality('Sleeveless Dress')
        assert pp.added_to_cart_text_visibility()==True

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
        for i in cp.product_description_text():
            if 'Men Tshirt' in i:
                has_tshirt = True
            if 'Sleeveless Dress' in i:
                has_dress = True

        if has_tshirt and has_dress:
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CART_004.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

        # assert 'Men Tshirt' in cp.product_description_text()
        # assert 'Sleeveless Dress' in cp.product_description_text()

    def test_AE_CART_005(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)
        cp=CartPage(self.driver)

        hp.click_product_button()

        pp.add_to_cart_functionality('Men Tshirt')
        assert pp.added_to_cart_text_visibility() == True

        pp.click_view_cart_button()
        for i in cp.product_description_text():
            if 'Men Tshirt' in i:
                assert True
        # assert 'Men Tshirt' in cp.product_description_text()

        cp.click_delete_item_button('Men Tshirt')
        if cp.cart_empty_text_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CART_005.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_CART_006(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)
        cp=CartPage(self.driver)

        hp.click_product_button()

        cart_count=pp.add_multiple_quantity_of_a_product(3,'Men Tshirt')
        hp.click_cart_button()

        total_cart_value=cart_count*pp.get_item_prices('Men Tshirt')

        for i in cp.get_cart_total_value():
            if total_cart_value==i:
                update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
                assert True
            else:
                self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CART_006.png')
                update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
                assert False

    def test_AE_CHECK_001(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)
        pp=ProductsPage(self.driver)
        cp=CartPage(self.driver)
        chp=CheckoutPage(self.driver)

        hp.click_login_signup_button()

        lp.enter_login_details(email='dummy69@gmail.com',password='dummy')
        lp.click_login_button()

        hp.click_product_button()

        pp.add_to_cart_functionality('Men Tshirt')
        pp.click_view_cart_button()

        assert cp.product_description_visibility()==True

        cp.click_proceed_to_checkout_button()

        if chp.review_order_text_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CHECK_001.png')
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'fail')
            assert False

    def test_AE_CHECK_002(self):
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        pp = ProductsPage(self.driver)
        cp = CartPage(self.driver)
        chp = CheckoutPage(self.driver)
        pap = PaymentPage(self.driver)

        hp.click_product_button()

        pp.add_to_cart_functionality('Men Tshirt')
        assert pp.added_to_cart_text_visibility() == True
        # pp.click_continue_shopping_button()
        pp.click_view_cart_button()

        hp.click_cart_button()

        cp.click_proceed_to_checkout_button()

        if cp.register_login_text_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CHECK_002.png')
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'fail')
            assert False

    def test_AE_CHECK_003(self):
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        pp = ProductsPage(self.driver)
        cp = CartPage(self.driver)
        chp = CheckoutPage(self.driver)
        pap = PaymentPage(self.driver)

        hp.click_login_signup_button()

        lp.enter_login_details(email='dummy69@gmail.com', password='dummy')
        lp.click_login_button()

        hp.click_product_button()

        pp.add_to_cart_functionality('Men Tshirt')
        assert pp.added_to_cart_text_visibility() == True
        # pp.click_continue_shopping_button()
        pp.click_view_cart_button()

        hp.click_cart_button()

        cp.click_proceed_to_checkout_button()

        if chp.your_delivery_address_text_visibility():
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CHECK_003.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_CHECK_004(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)
        pp=ProductsPage(self.driver)
        cp=CartPage(self.driver)
        chp=CheckoutPage(self.driver)

        hp.click_login_signup_button()

        lp.enter_login_details(email='dummy69@gmail.com',password='dummy')
        lp.click_login_button()

        hp.click_product_button()

        pp.add_to_cart_functionality('Men Tshirt')
        pp.click_view_cart_button()

        assert cp.product_description_visibility()==True

        cp.click_proceed_to_checkout_button()

        if cp.get_cart_description_text('Men Tshirt')==chp.get_product_description_text('Men Tshirt'):
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CHECK_004.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_CHECK_005(self):
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        pp = ProductsPage(self.driver)
        cp = CartPage(self.driver)
        chp = CheckoutPage(self.driver)
        pap = PaymentPage(self.driver)

        hp.click_login_signup_button()

        lp.enter_login_details(email='dummy69@gmail.com', password='dummy')
        lp.click_login_button()

        hp.click_product_button()

        pp.add_to_cart_functionality('Men Tshirt')
        assert pp.added_to_cart_text_visibility() == True
        # pp.click_continue_shopping_button()
        pp.click_view_cart_button()

        hp.click_cart_button()

        cp.click_proceed_to_checkout_button()

        chp.click_place_order_button()

        pap.enter_card_details('dummy', '12345678', '121', '11', '2030')
        pap.click_pay_confirm_button()

        if pap.order_placed_text_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CHECK_005.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_CONTACT_001(self):
        hp=HomePage(self.driver)
        cup=ContactUsPage(self.driver)

        hp.click_contact_us_button()

        if cup.contact_us_text_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CONTACT_001.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_CONTACT_002(self):
        hp=HomePage(self.driver)
        cup=ContactUsPage(self.driver)

        hp.click_contact_us_button()

        assert cup.contact_us_text_visibility()==True

        cup.enter_contact_us_details(name='dummy',email='dummy@gmail.com',subject='Testing',message='Testing1')
        cup.click_submit_button()
        cup.handling_alert()

        if cup.success_message_text_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CONTACT_002.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_CONTACT_003(self):
        hp=HomePage(self.driver)
        cup=ContactUsPage(self.driver)

        hp.click_contact_us_button()

        assert cup.contact_us_text_visibility()==True

        cup.enter_contact_us_details(name='dummy',email='dummy@gmail.com',subject='Testing',message='Testing1')
        cup.upload_file_functionality('D:\\Automation Excercise\\testdata\\AutomationExercise_60_Detailed_TestCases.xlsx')
        cup.click_submit_button()
        cup.handling_alert()

        if cup.success_message_text_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_CONTACT_003.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_SUB_001(self):
        hp=HomePage(self.driver)

        hp.scrolling_to_subscription_field()

        if hp.subscription_field_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_SUB_001.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_SUB_002(self):
        hp=HomePage(self.driver)

        hp.scrolling_to_subscription_field()

        hp.enter_subscription_email('dummy69@gmail.com')
        hp.click_subscribe_button()

        if hp.subscription_successful_message():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_SUB_002.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_SUB_003(self):
        hp=HomePage(self.driver)

        hp.scrolling_to_subscription_field()

        if hp.enter_invalid_subscription_email('dummy'):
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_SUB_003.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_ACC_001(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)
        sp=SignupPage(self.driver)

        hp.click_login_signup_button()

        lp.enter_signup_details("hmm", "hmm69@gmail.com")
        lp.click_signup_button()

        assert sp.account_information_text_visibility() == True
        sp.click_title_button("mr")
        sp.fill_all_the_fields("hmmm", "hmmm", "kumar", "abc", "Colony", "Bangalore", "Karnataka", "Urban", "112233",
                               "123456789")
        sp.select_date("15", "February", "2016")
        sp.select_country("India")
        sp.select_newsletter()
        sp.click_create_account_button()

        assert sp.account_created_text_visibility()==True

        hp.click_home_button()
        hp.click_delete_account_button()

        if hp.account_deleted_text_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_ACC_001.png')
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'fail')
            assert False

    def test_AE_ACC_002(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)
        sp=SignupPage(self.driver)

        hp.click_login_signup_button()

        lp.enter_signup_details("hmm", "hmm69@gmail.com")
        lp.click_signup_button()

        assert sp.account_information_text_visibility() == True
        sp.click_title_button("mr")
        sp.fill_all_the_fields("hmmm", "hmmm", "kumar", "abc", "Colony", "Bangalore", "Karnataka", "Urban", "112233",
                               "123456789")
        sp.select_date("15", "February", "2016")
        sp.select_country("India")
        sp.select_newsletter()
        sp.click_create_account_button()

        assert sp.account_created_text_visibility()==True

        hp.click_home_button()
        hp.click_delete_account_button()

        assert hp.account_deleted_text_visibility()==True

        hp.click_login_signup_button()

        lp.enter_login_details(email='hmm69@gmail.com',password='hmmm')

        if lp.wrong_email_password_text_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_ACC_002.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_ACC_003(self):
        hp=HomePage(self.driver)
        lp=LoginPage(self.driver)

        hp.click_login_signup_button()

        lp.enter_login_details(email='hm69@gmail.com',password='hmm')
        lp.click_login_button()

        if lp.incorrect_email_text_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_ACC_003.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_NAV_001(self):
        hp=HomePage(self.driver)

        hp.click_home_button()

        if hp.home_page_active_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_NAV_001.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_NAV_002(self):
        hp=HomePage(self.driver)
        tp=TestCasesPage(self.driver)

        hp.click_test_cases_button()

        if tp.list_of_test_cases_text_visibility():
            update_test_result(self.file,self.sheet,self.row+1,self.col,'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_NAV_002.png')
            update_test_result(self.file,self.sheet,self.row+1,self.col,'fail')
            assert False

    def test_AE_NAV_003(self):
        hp=HomePage(self.driver)

        hp.scrolling_to_subscription_field()

        hp.click_scroll_up_button()

        if hp.home_page_active_visibility():
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_NAV_003.png')
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'fail')
            assert False

    def test_AE_UI_046(self):
        hp=HomePage(self.driver)
        assert hp.page_title_visibility()==True
        if hp.page_title_clickable():
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_046.png')
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'fail')
            assert False

    def test_AE_UI_047(self):
        hp=HomePage(self.driver)

        assert hp.top_navigation_menu_visibility()==True

        if hp.necessary_top_navigation_menu_visibility():
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_047.png')
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'fail')
            assert False

    def test_AE_UI_048(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        hp.click_home_button()

        if pp.all_products_text_visibility():
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_048.png')
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'fail')
            assert False

    def test_AE_UI_049(self):
        hp=HomePage(self.driver)
        cp=CartPage(self.driver)

        hp.click_cart_button()

        if cp.cart_empty_text_visibility():
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_049.png')
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'fail')
            assert False

    def test_AE_UI_050(self):
        hp=HomePage(self.driver)

        hp.scrolling_to_subscription_field()

        if hp.footer_visibility():
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_050.png')
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'fail')
            assert False

    def test_AE_UI_051(self):
        hp=HomePage(self.driver)

        hp.scrolling_to_subscription_field()

        if hp.subscription_email_visibility():
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_051.png')
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'fail')
            assert False

    def test_AE_UI_052(self):
        hp=HomePage(self.driver)

        hp.scrolling_to_recommended_items()

        if hp.recommended_items_visibility():
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_052.png')
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'fail')
            assert False

    def test_AE_UI_053(self):
        hp=HomePage(self.driver)

        hp.scrolling_to_recommended_items()

        if hp.category_text_visibility():
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_053.png')
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'fail')
            assert False

    def test_AE_UI_054(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        pp.select_category('Women')
        pp.select_subcategory('Dress')

        if pp.category_selection_visibility():
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_054.png')
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'fail')
            assert False

    def test_AE_UI_055(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        assert pp.product_name_visibility()==True
        assert pp.product_price_visibility()==True
        assert pp.product_image_visibility()==True

    def test_AE_UI_056(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        hp.click_product_button()

        pp.click_view_product_button('Men Tshirt')

        if pp.quantity_text_visibility():
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_056.png')
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'fail')
            assert False

    def test_AE_UI_057(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        hp.click_product_button()

        pp.add_to_cart_hover('Men Tshirt')

        if pp.add_to_cart_visibility():
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_057.png')
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'fail')
            assert False

    def test_AE_UI_058(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        hp.click_product_button()

        pp.add_to_cart_functionality('Men Tshirt')

        assert pp.view_cart_button_text_visibility()==True
        assert pp.continue_shopping_button_text_visibility()==True

    def test_AE_UI_059(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)

        hp.click_product_button()

        pp.add_to_cart_functionality('Men Tshirt')

        pp.click_continue_shopping_button()

        if pp.all_products_text_visibility():
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_059.png')
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'fail')
            assert False

    def test_AE_UI_060(self):
        hp=HomePage(self.driver)
        pp=ProductsPage(self.driver)
        cp=CartPage(self.driver)

        hp.click_product_button()

        pp.add_to_cart_functionality('Men Tshirt')

        pp.click_view_cart_button()

        if cp.product_description_visibility():
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'pass')
            assert True
        else:
            self.driver.save_screenshot(os.curdir + '\\screenshots\\test_AE_UI_060.png')
            update_test_result(self.file, self.sheet, self.row+1, self.col, 'fail')
            assert False













