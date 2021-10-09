from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DeliveryLocation:

    def __init__(self, driver):
        self.driver = driver

    location_text_box = (By.ID, "country")
    drop_down_location = (By.LINK_TEXT, "India")
    terms_agreement = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit_btn = (By.CSS_SELECTOR, "[type='submit']")
    message = (By.CLASS_NAME, "alert-success")

    def location_box(self):
        return self.driver.find_element(*DeliveryLocation.location_text_box)

    def drop_location(self):
        return self.driver.find_element(*DeliveryLocation.drop_down_location)

    def agree_checkbox(self):
        return self.driver.find_element(*DeliveryLocation.terms_agreement)

    def submit_button(self):
        return self.driver.find_element(*DeliveryLocation.submit_btn)

    def verifySuccessMessage(self):
        return self.driver.find_element(*DeliveryLocation.message)

