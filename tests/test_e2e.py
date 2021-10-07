import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.checkout_page import CheckOut
from page_objects.homepage import HomePage
from utilities.BaseClass import BaseClass


class TestEndToEnd(BaseClass):

    def test_e2e(self):

        add_to_cart_item = []
        cart_items = []

        homePage = HomePage(self.driver)
        checkOut = CheckOut(self.driver)

        homePage.shop_item().click()

        list_of_products = checkOut.product_list()
        #self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for product in list_of_products:
            item_title = product.find_element(By.XPATH, "div/h4/a")
            item_btn = product.find_element(By.XPATH, "div/h4/a/../../../div/button")
            if item_title.text == "Blackberry":
                item_btn.click()
            add_to_cart_item.append(item_title.text)

        action = ActionChains(self.driver)

        checkout = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Checkout")

        time.sleep(3)

        action.move_to_element(checkout).click().perform()

        list_of_added_to_cart = self.driver.find_elements(By.XPATH, "//tr/td/div[@class='media']/div/h4")

        for list_to_cart in list_of_added_to_cart:
            cart_items.append(list_to_cart.text)

        assert "Blackberry" in cart_items

        self.driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]").click()

        self.driver.find_element(By.ID, "country").send_keys("Ind")

        wait = WebDriverWait(self.driver, 10)

        list_of_countries = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))

        list_of_countries.click()

        checkbox = self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']")

        checkbox.click()

        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

        success = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        assert "Success! Thank you!" in success

        self.driver.get_screenshot_as_file("screen.png")

