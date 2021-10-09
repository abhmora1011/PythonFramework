from selenium.webdriver.support.select import Select

from page_objects.homepage import HomePage
from utilities.BaseClass import BaseClass
from utilities.data_bank import TestData


class Test_HomePage(BaseClass):

    def test_formSubmission(self):

        homePage = HomePage(self.driver)

        homePage.name_field().send_keys(TestData.NAME)

        homePage.email_field().send_keys(TestData.EMAIL)

        homePage.password_field().send_keys(TestData.PASSWORD)

        self.selectOptionByText(homePage.gender_field(), TestData.GENDER)

        homePage.check_ice_cream().click()

        homePage.submit_button().click()

        message = homePage.success_text().text

        assert "Success" in message