import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    # Custom Utilities
    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))
        return element

    def selectOptionByText(self, by_locator, text):
        sel = Select(by_locator)
        sel.select_by_visible_text(text)

    def click_element_by_locator(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).click()


