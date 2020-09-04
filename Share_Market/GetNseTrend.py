import requests
import re
from bs4 import BeautifulSoup


class NseTrend(object):
    def __init__(self):
        self.url = "https://www.moneycontrol.com/stocksmarketsindia/"

    def get_trend(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        data_array = soup.find(id="nlp").getText().strip().split()[-1]
        trend = re.search(r'[-0123456]\d*.\d*', data_array)
        perc_trend = trend.group()
        return perc_trend
