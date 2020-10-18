import requests
from bs4 import BeautifulSoup


class NseTrend(object):
    def __init__(self):
        self.url = "https://www.moneycontrol.com/stocksmarketsindia/"

    def get_trend(self, sector):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        divs = soup.findAll("table", {"class": "mctable1"})
        nifty_trend = {}
        for div in divs:
            rows = div.findAll('tr')
            for row in rows:
                if sector in row.text:
                    column = row.findAll("td")
                    nifty_trend['index'] = column[0].text
                    nifty_trend['Price'] = column[1].text
                    nifty_trend['Change'] = column[2].text
                    nifty_trend['%Chg'] = column[3].text
                    break
        return nifty_trend


if __name__ == "__main__":
    obj = NseTrend()
    obj.get_trend("NIFTY BANK")