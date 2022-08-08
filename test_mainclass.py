import pytest
from selenium.webdriver.common.by import By

from pageObjects.homepage import HomePage
from utilities.usefixture import UseFixture

@pytest.mark.skip
class TestShopping(UseFixture):
    def test_product_select_verify(self):
        homePageObj = HomePage(self.webdriverObj)
        print(self.webdriverObj.title)
        homePageObj.search_bar().send_keys("summer dress")
        searchResultsPageObj = homePageObj.search_button()
        searchResultsPageObj.select_product().click()
        searchResultsPageObj.add_to_cart().click()

