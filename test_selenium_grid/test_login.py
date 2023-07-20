import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

def test_login(emulator_login):
    driver = emulator_login
    driver.implicitly_wait(10)
    driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="Username input field"]').send_keys("bob@example.com")
    driver.implicitly_wait(10)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@content-desc="Password input field"]').send_keys("10203040")
    driver.implicitly_wait(10)
    driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="Login button"]').click()
    driver.implicitly_wait(10)
    print("Done -->")





