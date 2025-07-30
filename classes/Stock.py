import yfinance as yf
import csv
import pandas as pd
from Option import Option

class Stock:

    def __init__(self, ticker: str):

        self.ticker = ticker.upper()

        self.data = yf.Ticker(self.ticker)
    
    def get_option_chain(self, expiration_index: int=0, export_chain:bool=False):

        options = self.data.options
        if not options:
            raise ValueError(f"OptionError: No options found for {self.ticker}.")
        expiration_date = options[expiration_index]
        chain = self.data.option_chain(expiration_date)
        if export_chain:
            with open(f"{self.ticker.lower()}_call_option_chain.csv", "w", newline="") as file:
                chain.calls.to_csv(file, index=False)
            with open(f"{self.ticker.lower()}_put_option_chain.csv", "w", newline="") as file:
                chain.puts.to_csv(file, index=False)
        return chain.calls, chain.puts
    

    def black_scholes_model(self, option: Option, call:bool=True):
        pass
        # if call:
        #     self.data[""]

    @property
    def get_current_price(self):
        return self.data.info["regularMarketPrice"]




msft = Stock(ticker="MSFT")
print(msft.get_current_price)
# msft_calls, msft_puts = msft.get_option_chain(expiration_index=0, export_chain=True)
# print(msft_calls)


