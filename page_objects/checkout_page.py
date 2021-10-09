from selenium.webdriver.common.by import By


class CheckOut:

    def __init__(self, driver):
        self.driver = driver

    list_of_products = (By.XPATH, "//div[@class='card h-100']")
    product_title = (By.XPATH, "//div[@class='card h-100']/div/h4")
    product_button = (By.XPATH, "//div[@class='card h-100']/div/button")
    checkout = (By.PARTIAL_LINK_TEXT, "Checkout")

    def item_title(self):
        return self.driver.find_elements(*CheckOut.product_title)

    def item_button(self):
        return self.driver.find_elements(*CheckOut.product_button)

    def checkout_button(self):
        return self.driver.find_element(*CheckOut.checkout)


