import json
import pandas as pd
from nsetools import Nse


class Nsedata(object):
    def __init__(self):
        self.nse = Nse()
        self.data = self.nse.get_preopen_nifty(as_json=True)

    @property
    def get_gap_up_scrips(self):
        data = json.loads(self.data)  # load the json string into python list obj
        df = pd.DataFrame(data)       # Create data frame obj
        df['perChn'] = df['perChn'].astype(float)  # convert perChn value to float
        df = df[df['perChn'] > 1.0]                # filter out the scrips if perChn > 1
        df = df[df['iep'] < 500]
        return df[['symbol', 'iep', 'pCls', 'chn', 'perChn']]

    @property
    def get_gap_down_scrips(self):
        data = json.loads(self.data)  # load the json string into python list obj
        df = pd.DataFrame(data)       # Create data frame obj
        df['perChn'] = df['perChn'].astype(float)  # convert perChn value to float
        df = df[df['perChn'] < -1.0]                # filter out the scrips if perChn > 1
        df = df[df['iep'] < 500]
        return df[['symbol', 'iep', 'pCls', 'chn', 'perChn']]