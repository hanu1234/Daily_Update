from appium import webdriver


class AndroidMobileWebTest:
    def __init__(self):
        desired_capabilities = {
            'platformName': 'Android',
            'platformVersion': '8.0.0',
            'deviceName': 'emulator-5554',
            'browserName': 'Chrome'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
        self.driver.get("https://www.facebook.com/")
        self.driver.find_element_by_id("m_login_email").send_keys("8971766359")
        self.driver.find_element_by_id("m_login_password").send_keys("viraths123@")

        self.driver.quit()


obj = AndroidMobileWebTest()
