import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

@pytest.fixture
def emulator_login():
    capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Pixel 3 API 30',
    udid='emulator-5554',
    app='/Users/masoodahmed/Desktop/Appium_Parallel_Testing_Selenium_Grid_4/app/Android-MyDemoAppRN.1.3.0.build-244.apk',
    platformVersion='11.0',
    )

    appium_server_url = 'http://localhost:4723'
    driver  = webdriver.Remote(appium_server_url, capabilities)
    driver.implicitly_wait(30)

    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='open menu').click()


    driver.implicitly_wait(10)

    driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Log In"]').click()

    driver.implicitly_wait(10)

    return driver