import time  #importaciones necesarias para ejecutar las pruebas
import data
import main
from selenium import webdriver


class TestSauceDemo:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_login(self):
        self.driver.get(data.URL_SAUCE)
        login = main.Login(self.driver)
        login.wait_for_load_field()
        login.set_username(data.USERNAME)
        login.set_password(data.PASSWORD)
        login.click_sign_up()

        assert data.URL_SAUCE == "https://www.saucedemo.com/"

    def test_add_product(self):
        self.test_login()
        add_product = main.AddProducts(self.driver)
        add_product.wait_for_load_field()
        add_product.backpack()
        add_product.bike_light()
        add_product.fleece()
        add_product.click_cart_button()

        assert data.URL_SAUCE == "https://www.saucedemo.com/"

    def test_shopping_cart(self):
        self.test_add_product()
        cart = main.ShoppingCart(self.driver)
        cart.wait_for_load_field()
        cart.click_checkout_button()

        assert data.URL_SAUCE == "https://www.saucedemo.com/"

    def test_checkout_info(self):
        self.test_shopping_cart()
        checkout = main.CheckoutInfo(self.driver)
        checkout.wait_for_load_field()
        checkout.set_first_name(data.FIRSTNAME)
        checkout.set_lastname(data.LASTNAME)
        checkout.set_postal_code(data.POSTAL_CODE)
        checkout.click_continue_button()

        assert data.URL_SAUCE == "https://www.saucedemo.com/"

    def test_finish_shopping(self):
        self.test_checkout_info()
        finish = main.FinishShopping(self.driver)
        finish.wait_for_load_field()
        finish.click_finish_button()

        assert data.URL_SAUCE == "https://www.saucedemo.com/"


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()





