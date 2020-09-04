import time
from GetGapUpandGapdown import Nsedata
from GetNseTrend import NseTrend
from GetScripsLiveData import Live
from selenium import webdriver
import pandas as pd
import csv


class AutoOrder(object):
    def __init__(self):
        self.trend = NseTrend()
        self.gap = Nsedata()
        self.live = Live()
        self.url = "https://kite.zerodha.com/"
        self.driver = None

    def open_browser(self):
        caps = webdriver.DesiredCapabilities.CHROME.copy()
        self.driver = webdriver.Chrome(desired_capabilities=caps)
        self.driver.maximize_window()
        self.driver.get(self.url)

    def login(self, username, password, pin):
        try:
            print("Entering user name:", username)
            self.driver.find_element_by_xpath("//input[@type='text']").clear()
            self.driver.find_element_by_xpath("//input[@type='text']").send_keys(username)
            self.driver.implicitly_wait(10)

            print("Entering the password", password)
            self.driver.find_element_by_xpath("//input[@type='password']").clear()
            self.driver.find_element_by_xpath("//input[@type='password']").send_keys(password)

            print("Clicking on the login button")
            self.driver.find_element_by_css_selector(".button-orange").click()
            self.driver.implicitly_wait(30)

            print("Entering the PIN", pin)
            self.driver.find_element_by_xpath("//input[@type='password']").clear()
            time.sleep(20)
            self.driver.find_element_by_xpath("//input[@type='password']").send_keys(pin)

            self.driver.implicitly_wait(30)
            print("Clicking on the continue button")
            self.driver.find_element_by_css_selector(".button-orange").click()
            self.driver.implicitly_wait(10)

            print(self.driver.title)
        except Exception as e:
            print(e)

    def analyze_gap_up_scrips(self):
        pass

    def get_analyzed_scrips(self):
        trend = self.trend.get_trend()
        print("Trend of the Market is {}".format(trend))
        gap_up_scrips = self.gap.get_gap_up_scrips
        print(gap_up_scrips)
        if float(trend) <= -0.25:
            gap_up_scrips = self.gap.get_gap_up_scrips
            scrips = gap_up_scrips.symbol.tolist()
            print("Gap Up Scrips Are:")
            for i in scrips:
                print(i)
                current_price, low, high = self.live.get_live_data(i)
                print(current_price, low, high)

        elif float(trend) >= 0.25:
            gap_down_scrips = self.gap.get_gap_down_scrips
            scrips = gap_down_scrips.symbol.tolist()
            for i in scrips:
                print(i)
                current_price, low, high = self.live.get_live_data(i)
                print(current_price, low, high)
        else:
            print("No Available scrips today")


obj = AutoOrder()
obj.get_analyzed_scrips()
