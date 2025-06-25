import time
import configuration
import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class EshopPage:
    search_input = (By.NAME, "q")  # Campo de búsqueda
    search_button = (By.XPATH, '//button[@aria-label="Search"]')
    product_tile = (By.CLASS_NAME, "product-card")
    add_to_cart_button = (By.XPATH, '//button[contains(text(), "Add to Bag")]')
    cart_icon = (By.XPATH, '//a[@aria-label="Bag"]')
    cart_items = (By.CLASS_NAME, "cart-item")
    checkout_button = (By.XPATH, '//button[contains(text(), "Checkout")]')
    checkout_page_title = (By.XPATH, '//h1[contains(text(), "Checkout")]')

    def __init__(self, driver):
        self.driver = driver

    def search_product(self, keyword):
        WebDriverWait(self.driver, configuration.WAIT_TIMEOUT).until(
            EC.presence_of_element_located(self.search_input)
        ).send_keys(keyword)
        self.driver.find_element(*self.search_button).click()

    def select_first_product(self):
        WebDriverWait(self.driver, configuration.WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(self.product_tile)
        ).click()

    def add_product_to_cart(self):
        WebDriverWait(self.driver, configuration.WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(self.add_to_cart_button)
        ).click()

    def go_to_cart(self):
        WebDriverWait(self.driver, configuration.WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(self.cart_icon)
        ).click()

    def get_cart_items(self):
        return WebDriverWait(self.driver, configuration.WAIT_TIMEOUT).until(
            EC.presence_of_all_elements_located(self.cart_items)
        )

    def click_checkout(self):
        WebDriverWait(self.driver, configuration.WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()

    def is_checkout_page_displayed(self):
        return WebDriverWait(self.driver, configuration.LONG_TIMEOUT).until(
            EC.visibility_of_element_located(self.checkout_page_title)
        )


class TestEshop:
    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        cls.driver = webdriver.Chrome(service=Service(), options=options)
        cls.driver.get(configuration.BASE_URL)

    def test_add_shoe_to_cart(self):
        eshop = EshopPage(self.driver)
        eshop.search_product(data.search_keyword)
        eshop.select_first_product()
        eshop.add_product_to_cart()
        eshop.go_to_cart()
        items = eshop.get_cart_items()
        assert len(items) > 0, "El carrito debería tener al menos un producto"

    def test_checkout_flow(self):
        eshop = EshopPage(self.driver)
        eshop.search_product(data.search_keyword)
        eshop.select_first_product()
        eshop.add_product_to_cart()
        eshop.go_to_cart()
        eshop.click_checkout()
        assert eshop.is_checkout_page_displayed(), "No se mostró la página de checkout"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
