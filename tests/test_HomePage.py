import pytest
from selenium.webdriver.support.select import Select

from page_objects.homepage import HomePage
from utilities.BaseClass import BaseClass
from utilities.data_bank import TestData


class Test_HomePage(BaseClass):

    def test_formSubmission(self, get_data):

        homePage = HomePage(self.driver)

        homePage.name_field().send_keys(get_data[0])

        homePage.email_field().send_keys(get_data[1])

        homePage.password_field().send_keys(TestData.PASSWORD)

        self.selectOptionByText(homePage.gender_field(), get_data[2])

        homePage.check_ice_cream().click()

        homePage.submit_button().click()

        message = homePage.success_text().text

        assert "Success" in message

        self.driver.refresh()

    @pytest.fixture(params=[("Abraham Ora", "abraham.morial.ora@gmail.com", "Male"), ("Clarisse Ora", "clarisse.licuanan.ora@gmail.com", "Female") ])
    def get_data(self, request):
        return request.param