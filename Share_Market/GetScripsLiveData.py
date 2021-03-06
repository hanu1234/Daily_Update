import requests
import pandas as pd


class Live(object):
    def __init__(self):
        self.url = "https://www.moneycontrol.com/stocks/marketstats/nsegainer/index.php"

    def get_live_data(self):
        response = requests.get(self.url).content
        pd.set_option('display.max_columns', None)
        df_list = pd.read_html(response)
        df = df_list[0]
        top_gainer_data = {'company_names': [], 'High': [], 'Low': [], 'Gain': [], 'Last_Price': [], 'Prev_Close': []}

        company_name = df['Company Name'][0::7]
        for company in company_name:
            top_gainer_data['company_names'].append(" ".join(company.split()[0:2]))

        for high in df['High'][0::7]:
            top_gainer_data['High'].append(high)

        for low in df['Low'][0::7]:
            top_gainer_data['Low'].append(low)

        for gain in df['% Gain'][0::7]:
            top_gainer_data['Gain'].append(gain)

        for last_price in df['Last Price'][0::7]:
            top_gainer_data['Last_Price'].append(last_price)

        for close in df['Prev Close'][0::7]:
            top_gainer_data['Prev_Close'].append(close)

        df = pd.DataFrame(top_gainer_data)
        print(df)


if __name__ == "__main__":
    obj = Live()
    obj.get_live_data()
