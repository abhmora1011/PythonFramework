from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[text()='Shop']")


    def shop_item(self):
        return self.driver.find_element(*HomePage.shop) # * to treat the variable as a tuple and deserialize
        #   driver.find_element(By.CSS_SELECTOR, "//a[text()='Shop']")




