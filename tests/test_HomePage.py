import pytest

from page_objects.homepage import HomePage
from test_data.HomePageData import HomePageData
from utilities.BaseClass import BaseClass
from test_data.data_bank import TestData


class Test_HomePage(BaseClass):

    def test_formSubmission(self, get_data):
        homePage = HomePage(self.driver)

        homePage.name_field().send_keys(get_data["fullname"])

        homePage.email_field().send_keys(get_data["email"])

        homePage.password_field().send_keys(TestData.PASSWORD)

        self.selectOptionByText(homePage.gender_field(), get_data["gender"])

        homePage.check_ice_cream().click()

        #self.click_element_by_locator(homePage.submit)
        homePage.submit_button().click()

        message = homePage.success_text().text

        assert "Success" in message

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_homepage_data)
    def get_data(self, request):
        return request.param
