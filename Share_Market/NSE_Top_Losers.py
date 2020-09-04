import json
import pandas as pd
from nsetools import Nse


class Losers(object):
    def __init__(self):
        self.nse = Nse()
        self.data = self.nse.get_top_losers(as_json=True)

    @property
    def top_losers(self):
        data = json.loads(self.data)
        df = pd.DataFrame(data)
        df = df[df['openPrice'] < 400]
        return df[['symbol', 'openPrice', 'highPrice', 'lowPrice', 'netPrice']]


obj = Losers()
m = obj.top_losers
print(m)