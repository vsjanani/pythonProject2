import inspect
import pytest
from PycharmProjects.PycharmProjects.pythonProject2.data.practicecreateaccountdata import CreateAccountData
from PycharmProjects.PycharmProjects.pythonProject2.pageObjects.locators import Locator
from PycharmProjects.PycharmProjects.pythonProject2.pageObjects.practiceamazondropdown import PracticeAmazonDropDown
from PycharmProjects.PycharmProjects.pythonProject2.pageObjects.practicecreateaccountpage import CreateAccountPage
from PycharmProjects.PycharmProjects.pythonProject2.pageObjects.startherelink import StartHere
from PycharmProjects.PycharmProjects.pythonProject2.utilities.usefixture import UseFixture

amazonDropDownObj = None
createAccountPageObj = None
log = None


class TestPracticeMainClass(UseFixture):

    def test_dropDownValidation(self):
        global amazonDropDownObj, log
        amazonDropDownObj = PracticeAmazonDropDown(self.webdriverObj)
        amazonDropDownObj.drop_down().click()
        self.select_option(amazonDropDownObj.drop_down(), "Amazon Devices")
        log = self.logging()
        log.info("amazon devices is selected")

    def test_startHereLink(self):
        self.mouseHover.move_to_element(amazonDropDownObj.account_lists()).perform()
        # time.sleep(3)
        log.info(amazonDropDownObj.account_lists().text)
        # amazonDropDownObj.account_lists().click()
        startHereLink = StartHere(self.webdriverObj)
        self.expWait(Locator.start_Here)
        startHereLink.start_here().click()
        log.info("clicked link")

    def test_createAccount(self, get_createAccount_data):
        global createAccountPageObj
        createAccountPageObj = CreateAccountPage(self.webdriverObj)
        createAccountPageObj.yourName.send_keys(get_createAccount_data["Your name"])
        log.info(createAccountPageObj.yourName.get_attribute("value"))
        createAccountPageObj.mobileNumber.send_keys(get_createAccount_data["Mobile number"])
        createAccountPageObj.emailOptional.send_keys(get_createAccount_data["Email"])
        createAccountPageObj.passWord.send_keys(get_createAccount_data["Password"])
        errorMessageObj = createAccountPageObj.get_continue_field()
        assert get_createAccount_data["Email"] in errorMessageObj.failureMessage.text
        # assert "janani" in errorMessageObj.failureMessage.text  //this is to assess if failed screenshot is populted.
        self.check = self.expWait(Locator.your_Name)
        print(self.check)

    @pytest.fixture(params=CreateAccountData.getExcelData("test_createAccount"))
    def get_createAccount_data(self, request):
        # print(CreateAccountData.createAccountData[0].get("Your name"))
        return request.param








