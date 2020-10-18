import time
import csv
import os
from datetime import datetime
from Share_Market.GetNseTrend import NseTrend
from Share_Market.live_top_gainers import LiveGainers
from Share_Market.live_top_loosers import LiveLoosers


class Analysis:
    def __init__(self):
        self.trend = NseTrend()
        self.gainers = LiveGainers()
        self.loosers = LiveLoosers()
        self.target_data = []
        self.captured_time = []
        self.current_trend = []
        self.nifty_bank_trend = []

        # Scrips Ranges
        self.scrips_100_200 = None
        self.scrips_200_400 = None
        self.scrips_400_600 = None
        self.scrips_600_800 = None

    @property
    def get_current_trend(self):
        return self.trend.get_trend('NIFTY 50')['%Chg']

    def data_analysis(self):
        """
        - Based on the trend this method will go and analyse the market
        - Trend is > 0.3 bullish trend
        - Trend < 0.3 bearish trend
        """
        # create a directory to store the data
        dir_name = self.get_current_date_time("%Y-%m-%d")
        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)

        while True:
            trend = self.get_current_trend
            print(trend)
            if float(trend) >= 0.3:
                print("Market trend is bullish")
                self.analyse_bullish_market()

            elif float(trend) <= -0.3:
                print("Market trend is Bearish")
                self.analyse_bearish_market()

            else:
                print("Market Trend is Neutral")

            print("Waiting for 2 minutes....")
            time.sleep(120)

    def get_the_scrips(self):
        """
        - This will fill the scrips based on the value
        """
        df = self.gainers.get_live_data()
        df_100_200 = df[(df.High.astype(float) >= 100) & (df.High.astype(float) <= 200)]
        df_200_400 = df[(df.High.astype(float) >= 200) & (df.High.astype(float) <= 400)]
        df_400_600 = df[(df.High.astype(float) >= 400) & (df.High.astype(float) <= 600)]
        df_600_800 = df[(df.High.astype(float) >= 600) & (df.High.astype(float) <= 800)]

        self.scrips_100_200 = {i: [] for i in df_100_200['company_names'].to_list()}
        self.scrips_200_400 = {i: [] for i in df_200_400['company_names'].to_list()}
        self.scrips_400_600 = {i: [] for i in df_400_600['company_names'].to_list()}
        self.scrips_600_800 = {i: [] for i in df_600_800['company_names'].to_list()}

    def update_live_scrips_live_price(self, df, scrips, req_diff, m_trend):
        """

        """
        for company in scrips:
            df1 = df.loc[df['company_names'] == company]
            if not df1.empty:
                scrips[company].append(df1['Last_Price'].tolist()[0])
            else:
                scrips[company].append(0)

        time_now = self.get_current_date_time(time_format="%H:%M")
        self.captured_time.append(time_now)
        self.get_data_diff(scrips, self.current_trend, self.captured_time, req_diff, m_trend)

    def analyse_bullish_market(self):
        """
        - Need to fill
        """
        self.get_the_scrips()
        while True:
            df = self.gainers.get_live_data()
            self.current_trend.append(self.get_current_trend)
            self.nifty_bank_trend.append(self.trend.get_trend('NIFTY BANK')['%Chg'])
            print(f"{50*'*'}")
            print(f"NIFTY 50 Trend   -->{self.current_trend}")
            print(f"Nifty BANK Trend --> {self.nifty_bank_trend}")
            print(f"{50 * '*'}")

            self.update_live_scrips_live_price(df, self.scrips_100_200, 0, 'bullish')
            self.update_live_scrips_live_price(df, self.scrips_200_400, 2, 'bullish')
            self.update_live_scrips_live_price(df, self.scrips_400_600, 3, 'bullish')
            self.update_live_scrips_live_price(df, self.scrips_600_800, 4, 'bullish')
            time.sleep(3)

    def analyse_bearish_market(self):
        self.get_the_scrips()

        while True:
            df = self.loosers.get_live_data()
            self.current_trend.append(self.get_current_trend)
            self.nifty_bank_trend.append(self.trend.get_trend('NIFTY BANK')['%Chg'])
            print(f"{50*'*'}")
            print(f"NIFTY 50 Trend   -->{self.current_trend}")
            print(f"Nifty BANK Trend --> {self.nifty_bank_trend}")
            print(f"{50 * '*'}")

            self.update_live_scrips_live_price(df, self.scrips_100_200, 1, 'bearish')
            self.update_live_scrips_live_price(df, self.scrips_200_400, 2, 'bearish')
            self.update_live_scrips_live_price(df, self.scrips_400_600, 3, 'bearish')
            self.update_live_scrips_live_price(df, self.scrips_600_800, 4, 'bearish')
            time.sleep(300)

    def validate_data(self, diff, key, diff_value):
        if diff >= diff_value:
            if key not in self.target_data:
                self.target_data.append(key)
                return True

    def get_data_diff(self, data, trend, c_time, req_diff, m_trend):
        for key, value in data.items():
            print(f"{key} --> {value}")

        for key, value in data.items():
            if m_trend == "bullish":
                actual_diff = float(float(value[-1] - value[0]))
            else:
                actual_diff = float(float(value[0] - value[-1]))

            if self.validate_data(actual_diff, key, req_diff):
                print(f"{key} target reached")
                self.write_to_csv_file(key, value, trend, c_time)
        print(f"{50*'+'}")

    def write_to_csv_file(self, key, value, trend, c_time):
        data_dir = self.get_current_date_time("%Y-%m-%d")
        file = f"{data_dir}/{key}_data.csv"
        with open(file, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(c_time)
            csvwriter.writerow(trend)
            csvwriter.writerow(value)

    @staticmethod
    def get_current_date_time(time_format="%Y-%m-%d %H:%M"):
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
