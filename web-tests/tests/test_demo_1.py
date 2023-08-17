from selenium import webdriver
import time


def test_one():
    firefox_options = webdriver.FirefoxOptions()
    grid_url = "http://localhost:4444"

    driver = webdriver.Remote(
        command_executor= grid_url,
        options=firefox_options
    )

    # Perform your tests
    driver.get("http://www.google.com")
    # time.sleep(60)

    print("Test 1")
    print(driver.title)
    # time.sleep(60)
    driver.quit()