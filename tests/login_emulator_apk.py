import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
# from '../appium_config.py' import appium_config

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Pixel 3 API 30',
    udid='emulator-5554',
    app='/Users/masoodahmed/Desktop/Appium_Parallel_Testing_Selenium_Grid_4/app/Android-MyDemoAppRN.1.3.0.build-244.apk',
    platformVersion='11.0',
    # appPackage='com.android.settings',
    # appActivity='.Settings',
)

appium_server_url = 'http://localhost:4723'
# driver = webdriver.Remote(appium_server_url, appium_config)
driver  = webdriver.Remote(appium_server_url, capabilities)

driver.implicitly_wait(30)

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='open menu').click()


driver.implicitly_wait(10)

driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Log In"]').click()

driver.implicitly_wait(10)

driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="Username input field"]').send_keys("bob@example.com")

driver.implicitly_wait(10)

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@content-desc="Password input field"]').send_keys("10203040")

driver.implicitly_wait(10)

driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="Login button"]').click()

print("Done -->")

# class TestAppium(unittest.TestCase):
#     def setUp(self) -> None:
#         self.driver = webdriver.Remote(appium_server_url, capabilities)

#     def tearDown(self) -> None:
#         if self.driver:
#             self.driver.quit()

#     def test_find_battery(self) -> None:
#         el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
#         el.click()

# if __name__ == '__main__':
#     unittest.main()