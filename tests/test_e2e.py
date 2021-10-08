import time

from selenium.webdriver import ActionChains

# Pulling of Objects from Class


from page_objects.checkout_page import CheckOut
from page_objects.confirm_page import ConfirmPage
from page_objects.delivery_location import DeliveryLocation
from page_objects.homepage import HomePage
from utilities.BaseClass import BaseClass


class TestEndToEnd(BaseClass):

    def test_e2e(self):

        homePage = HomePage(self.driver)
        homePage.shop_item().click()

        checkOut = CheckOut(self.driver)
        confirmCart = ConfirmPage(self.driver)
        locationDelivery = DeliveryLocation(self.driver)

        product_titles = checkOut.item_title()
        product_button = checkOut.item_button()
        checkout = checkOut.checkout_button()

        add_to_cart_item = []
        i = -1
        for product in product_titles:
            i = i + 1
            if product.text == "Blackberry":
                product_button[i].click()
                # print("Blackberry")
            add_to_cart_item.append(product.text)

        action = ActionChains(self.driver)

        try:
            action.move_to_element(checkout).click().perform()
        except:
            print("Not clicked")

        list_cart = confirmCart.cart_list()

        cart_items = []
        for list_in_cart in list_cart:
            cart_items.append(list_in_cart.text)

        assert "Blackberry" in cart_items

        checkoutBtn = confirmCart.checkout_confirm()

        checkoutBtn.click()

        location = locationDelivery.location_box()

        location.send_keys("Ind")

        locationDelivery.verifyLinkPresence("India").click()

        locationDelivery.agree_checkbox().click()

        locationDelivery.submit_button().click()

        message = locationDelivery.verifySuccessMessage().text

        assert "Success! Thank you!" in message
