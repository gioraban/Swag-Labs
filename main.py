# importaciones necesarias para ejecutar las funciones
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Login: #se coloca en las casillas los datos requridos del login del usuario
    username_field = (By.XPATH, '//*[@id="user-name"]')
    password_field = (By.XPATH, '//*[@id="password"]')
    login_button = (By.XPATH, '//*[@id="login-button"]')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_field(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.username_field))

    def set_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_sign_up(self):
        self.driver.find_element(*self.login_button).click()

class AddProducts: #se agrega los productos al carrito y luego cambia a la ventana del cart
    add_backpack = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    add_bike_light = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    add_fleece = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
    car_button = (By.ID, 'shopping_cart_container')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_field(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.add_backpack))

    def backpack(self):
        self.driver.find_element(*self.add_backpack).click()

    def bike_light(self):
        self.driver.find_element(*self.add_bike_light).click()

    def fleece(self):
        self.driver.find_element(*self.add_fleece).click()

    def click_cart_button(self):
        self.driver.find_element(*self.car_button).click()

class ShoppingCart:
    checkout_button = (By.ID, 'checkout')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_field(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.checkout_button))

    def click_checkout_button(self):
        self.driver.find_element(*self.checkout_button).click()

class CheckoutInfo:
    first_name_field = (By.ID, 'first-name')
    last_name_field = (By.ID, 'last-name')
    postal_code_field = (By.ID, 'postal-code')
    continue_button = (By.ID, 'continue')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_field(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.first_name_field))

    def set_first_name(self, firstname):
        self.driver.find_element(*self.first_name_field).send_keys(firstname)

    def set_lastname(self, lastname):
        self.driver.find_element(*self.last_name_field).send_keys(lastname)

    def set_postal_code(self, postal_code):
        self.driver.find_element(*self.postal_code_field).send_keys(postal_code)

    def click_continue_button(self):
        self.driver.find_element(*self.continue_button).click()


class FinishShopping:
    finish_button = (By.ID, 'finish')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_field(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.finish_button))

    def click_finish_button(self):
        self.driver.find_element(*self.finish_button).click()




