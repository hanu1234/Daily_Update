"""
If we want select from the list of available options from the drop down, selenium API provides the Select class
there are two selection options in the drop down.
1. single select option
2. multi-select options

Select the drop down element by below select attributes.
1. index
2. value
3. text

Deselecting the options from drop down
1. deselect_all() clear all selected options, only applicable for multi selected drop down
2. deselect_by_index('idx')
3. deselect_by_value('value')
4. deselect_by_visible_text('text')

https://www.toolsqa.com/automation-practice-form/
in the above website select the continent from the continents drop down

@ for any Questions
Mail Me: hanamantds@gmail.com or call me:8971766359

"""
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


class SelectOptions(object):
    def __init__(self):
        self.url = "https://www.toolsqa.com/automation-practice-form/"
        chrome_options = Options()
        self.driver = webdriver.Chrome(options=chrome_options)      # creating chrome driver instance
        self.driver.get(self.url)                                   # opening the page
        sleep(2)
        self.driver.maximize_window()                               # maximizing the chrome window

    def select_option(self, label):
        s1 = Select(self.driver.find_element_by_id("continents"))   # Creating the select instance on the drop down obj

        # available options  are
        for opt in s1.options:
            print(opt.text)

        # select by index
        s1.select_by_index(2)

        # select by value
        s1.select_by_value("SA")

        # select by visible text
        s1.select_by_visible_text("Australia")

    def teardown(self):
        self.driver.quit()


if __name__ == "__main__":
    obj = SelectOptions()
    obj.select_option('xyz')
    obj.teardown()

