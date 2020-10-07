import requests
import pandas as pd


class LiveLoosers(object):
    def __init__(self):
        self.url = "https://www.moneycontrol.com/stocks/marketstats/nseloser/index.php"

    def get_live_data(self):
        response = requests.get(self.url).content
        pd.set_option('display.max_columns', None)
        df_list = pd.read_html(response)
        df = df_list[0]
        print(df.columns)
        live_data = {'company_names': [], 'High': [], 'Low': [], 'Loss': [], 'Last_Price': [], 'Prev_Close': []}

        company_name = df['Company Name'][0::7]
        for company in company_name:
            live_data['company_names'].append(" ".join(company.split()[0:2]))

        for high in df['High'][0::7]:
            live_data['High'].append(high)

        for low in df['Low'][0::7]:
            live_data['Low'].append(low)

        for gain in df['% Loss'][0::7]:
            live_data['Loss'].append(gain)

        for last_price in df['Last Price'][0::7]:
            live_data['Last_Price'].append(last_price)

        for close in df['Prev Close'][0::7]:
            live_data['Prev_Close'].append(close)

        df = pd.DataFrame(live_data)
        return df


if __name__ == "__main__":
    obj = LiveLoosers()
    obj.get_live_data()
