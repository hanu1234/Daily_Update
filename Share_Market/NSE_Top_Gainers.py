import json
import pandas as pd
from nsetools import Nse


class Gainers(object):
    def __init__(self):
        self.nse = Nse()
        self.data = self.nse.get_top_gainers(as_json=True)

    @property
    def top_gainers(self):
        data = json.loads(self.data)
        df = pd.DataFrame(data)
        df = df[df['openPrice'] < 300]
        return df[['symbol', 'openPrice', 'highPrice', 'lowPrice', 'netPrice']]


obj = Gainers()
m = obj.top_gainers
print(m)