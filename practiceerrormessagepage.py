from selenium.webdriver.common.by import By

from pageObjects.locators import Locator


class ErrorMessagePage:
    def __init__(self, webdriverObj):
        self.webdriverObj = webdriverObj
        self.failureMessage = self.webdriverObj.find_element(*Locator.failure_Message)

    # def get_failureMessage_field(self):
    #     return self.failureMessage

