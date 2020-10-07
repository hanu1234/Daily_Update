from Share_Market.GetNseTrend import NseTrend
from Share_Market.live_top_gainers import LiveGainers
from Share_Market.live_top_loosers import LiveLoosers
import time
from datetime import datetime
import csv


class Analysis:
    def __init__(self):
        self.trend = NseTrend()
        self.gainers = LiveGainers()
        self.loosers = LiveLoosers()
        self.target_data = []
        self.captured_time = []
        self.current_trend = []

    @property
    def get_current_trend(self):
        return self.trend.get_trend()['%Chg']

    def data_analysis(self):
        trend = self.trend.get_trend
        print(trend)
        if float(trend['%Chg']) >= 0.3:
            print("Market trend is bullish")
            self.analyse_bullish_market()

        elif float(trend['%Chg']) <= -0.3:
            print("Market trend is Bearish")

        else:
            print("Market Trend is Neutral")

    def analyse_bullish_market(self):
        df = self.gainers.get_live_data()
        df_new = df[df.High.astype(float) < 600]
        company_live_prices = {}
        for company in df_new['company_names']:
            company_live_prices[company] = []

        while True:
            df = self.gainers.get_live_data()
            df_new = df[df.High.astype(float) < 600]
            for company in df_new['company_names']:
                df1 = df_new.loc[df_new['company_names'] == company]
                company_live_prices[company].append(df1['Last_Price'].tolist()[0])

            self.current_trend.append(self.get_current_trend)
            time_now = self.get_current_date_time(time_format="%H:%M")
            self.captured_time.append(time_now)
            self.get_bullish_data_diff(company_live_prices, self.current_trend, self.captured_time)
            time.sleep(300)

    def validate_data(self, diff, key):
        if diff >= 2:
            self.target_data.append(key)
            if key not in self.target_data:
                return True

    def get_bullish_data_diff(self, data, trend, c_time):
        print(data)
        for key, value in data.items():
            diff = float(float(value[-1] - value[0]))
            if self.validate_data(diff, key):
                print(f"{key} target reached")
                self.write_to_csv_file(key, value, trend, c_time)

    def analyse_bearish_market(self):
        pass

    def write_to_csv_file(self, key, value, trend, c_time):
        time_format = "%Y_%m_%d_%H_%M"
        now = datetime.now()
        date_time = now.strftime(time_format)
        file = f"{key}_data {date_time}.csv"

        with open(file, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(c_time)
            csvwriter.writerows(trend)
            csvwriter.writerows(value)

    def get_current_date_time(self, time_format="%Y-%m-%d %H:%M"):
        """
        - Get current date with %Y-%m-%d %H:%M format

        :param time_format: default time format
        :return: current date with %Y-%m-%d %H:%M format
        """
        now = datetime.now()
        date_time = now.strftime(time_format)
        return date_time


if __name__ == "__main__":
    obj = Analysis()
    obj.data_analysis()
