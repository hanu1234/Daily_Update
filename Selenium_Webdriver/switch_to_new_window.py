"""
when you click on the any button some time new window will open.
for switch between the windows we need to use the windows handler.
1. self.driver.window_handles   --> return the list of all opened windows objects
2. for switch windows loop over these objects
3. self.driver.switch_to.window(window) --> window is the handler object. focus will go to the handler object window
Example:
    1. Go to naukari website
    2. click on the jobs button
    3. new window will open
    4. then switch to new window
    5. switch back to original window

@ for any Questions
Mail me: hanamantds@gmail.com
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


class SwitchWindow(object):
    def __init__(self):
        self.url = "https://www.naukri.com/"
        chrome_options = Options()
        chrome_options.add_argument("--disable-popup-blocking")   # disable the pop ups
        self.driver = webdriver.Chrome(options=chrome_options)    # creating chrome driver instance
        self.driver.get(self.url)                                 # opening the page
        sleep(2)
        self.driver.maximize_window()                             # maximizing the chrome window
        self.home_window = self.driver.current_window_handle

    def switch_window(self):
        # click on jobs button
        self.driver.find_element_by_css_selector(".mTxt").click()  # when we click on job section another window open

        # get the window handler
        handler = self.window_handlers
        print(handler)

        # loop over all window and print the title of the page
        for window in handler:
            self.driver.switch_to.window(window)
            print(self.driver.title)

        # switch to main page
        self.driver.switch_to.window(self.home_window)
        print(self.driver.title)

    @property
    def window_handlers(self):
        return self.driver.window_handles  # Returns the handles of all windows within the current session

    def teardown(self):
        self.driver.quit()  # close all the opened windows

if __name__ == "__main__":
    obj = SwitchWindow()
    obj.switch_window()
    obj.teardown()
