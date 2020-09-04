import requests
from bs4 import BeautifulSoup
import json


class Live(object):
    def __init__(self):
        self.url = "https://www.nse-india.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol="

    def get_live_data(self, symbol):
        url = self.url + symbol
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        data = soup.find(id="responseDiv").getText().strip()
        data = json.loads(data)
        current_price = data['data'][0]['buyPrice1']
        current_low = data['data'][0]['dayLow']
        current_high = data['data'][0]['dayHigh']
        return current_price, current_low, current_high


if __name__ == "__main__":
    obj = Live()
    obj.get_live_data("ZEEL")