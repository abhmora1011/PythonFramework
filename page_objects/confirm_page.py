from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    list_of_item_in_cart = (By.XPATH, "//tr/td/div[@class='media']/div/h4")
    checkout_confirmation = (By.XPATH, "//button[contains(text(),'Checkout')]")

    def cart_list(self):
        return self.driver.find_elements(*ConfirmPage.list_of_item_in_cart)

    def checkout_confirm(self):
        return self.driver.find_element(*ConfirmPage.checkout_confirmation)