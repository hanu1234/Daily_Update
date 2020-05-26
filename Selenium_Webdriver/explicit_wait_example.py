from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class ExplicitWait():

    def test(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Chrome()
        driver.implicitly_wait(.5)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.save_screenshot()

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.ID,
                                                         "stopFilter_stops-0")))
        element.click()

        driver.quit()
