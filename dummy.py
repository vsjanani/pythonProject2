import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

serviceObj = Service("/usr/bin/chromedriver")
webdriverObj = webdriver.Chrome(service=serviceObj)
webdriverObj.maximize_window()
webdriverObj.implicitly_wait(20)
webdriverObj.get("https://www.amazon.in")
mouseHover = ActionChains(webdriverObj)
mouseHover.move_to_element(webdriverObj.find_element(By.ID, "nav-link-accountList")).perform()
time.sleep(3)
webdriverObj.find_element(By.PARTIAL_LINK_TEXT, "Start here").click()
time.sleep(1)
myloc = (By.CSS_SELECTOR, "input[name='customerName']")
webdriverObj.find_element(By.CSS_SELECTOR, "input[name='customerName']").send_keys("janani")
print(webdriverObj.find_element(*myloc).get_attribute("value"))
webdriverObj.find_element(By.ID, "ap_phone_number").send_keys("123")
webdriverObj.find_element(By.CSS_SELECTOR, "[type='email']").send_keys("123@123.com")
webdriverObj.find_element(By.ID, "ap_password").send_keys("123456")
webdriverObj.find_element(By.CSS_SELECTOR, "#auth-continue").click()
# amazonObj = PracticeAmazonDropDown(webdriverObj)
expWait = WebDriverWait(webdriverObj, 10).until(expected_conditions.presence_of_element_located(myloc)).get_attribute("value")
# print(webdriverObj.find_element(*myloc).get_attribute("value"))
print(expWait)


# webdriverObj.get("http://automationpractice.com/index.php")
# webdriverObj.find_element(By.CSS_SELECTOR, "#search_query_top").send_keys("summer dress")
# mouseHover = ActionChains(webdriverObj)
# webdriverObj.find_element(By.CSS_SELECTOR, "button[name = 'submit_search']").click()
# webdriverObj.find_element(By.XPATH, '//div[@id = "center_column"]/ul/li[1]').click()
# webdriverObj.find_element(By.CSS_SELECTOR, "a[title = 'Add to cart']").click()
# mouseHover.move_to_element(webdriverObj.find_element(By.XPATH, '//div[@id = "c],.lk= 'Add to cart']")).click().perform()
#*****************************


