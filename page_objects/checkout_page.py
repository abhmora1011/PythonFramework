from selenium.webdriver.common.by import By


class CheckOut:

    def __init__(self, driver):
        self.driver = driver

    list_of_products = (By.XPATH, "//div[@class='card h-100']")

    def product_list(self):
        return self.driver.find_elements(*CheckOut.list_of_products)