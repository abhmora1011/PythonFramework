from selenium.webdriver.common.by import By

from page_objects.checkout_page import CheckOut


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[text()='Shop']")
    name = (By.NAME, "name")
    email = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.XPATH, "//input[@id='exampleInputPassword1']")
    gender = (By.ID, "exampleFormControlSelect1")
    check_box = (By.ID, "exampleCheck1")
    submit = (By.XPATH, "//input[@type='submit']")
    success = (By.CLASS_NAME, "alert-success")

    def shop_item(self):
        self.driver.find_element(*HomePage.shop).click() # * to treat the variable as a tuple and deserialize
        check_out = CheckOut(self.driver) # dito nalang nag initiate ng object para kay checkout page
        return check_out

    def name_field(self):
        return self.driver.find_element(*HomePage.name)

    def email_field(self):
        return self.driver.find_element(*HomePage.email)

    def password_field(self):
        return self.driver.find_element(*HomePage.password)

    def gender_field(self):
        return self.driver.find_element(*HomePage.gender)

    def check_ice_cream(self):
        return self.driver.find_element(*HomePage.check_box)

    def submit_button(self):
        return self.driver.find_element(*HomePage.submit)

    def success_text(self):
        return self.driver.find_element(*HomePage.success)