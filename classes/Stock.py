import yfinance as yf
import csv
import pandas as pd
from Option import Option
import math
from scipy.stats import norm
import numpy as np


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
        return expiration_date, chain.calls, chain.puts
    

    def black_scholes_model(self, option: Option, rate:float, call:bool=True):
        S = self.get_current_price
        K = option.strike
        T = option.days_until_expiration / 365.0
        r = r
        sigma = option.implied_volatility
        d1 = (math.log(S/K) + (r + sigma**2 / 2) * T) / (sigma * math.sqrt(T))
        d2 = d1 - (sigma * math.sqrt(T))

        if call:
            return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
        else:
            return K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

        

    @property
    def get_current_price(self):
        return self.data.info["regularMarketPrice"]




msft = Stock(ticker="MSFT")
expiration_date, msft_calls, msft_puts = msft.get_option_chain(expiration_index=0, export_chain=True)

calls = []

for _, row in msft_calls.iterrows():
    option = Option(
        contract_symbol=row["contractSymbol"],
        last_trade_date=row["lastTradeDate"],
        strike=row["strike"],
        last_price=row["lastPrice"],
        bid=row["bid"],
        ask=row["ask"],
        change=row["change"],
        percent_change=row["percentChange"],
        volume=row["volume"],
        open_interest=row["openInterest"],
        implied_volatility=row["impliedVolatility"],
        in_the_money=row["inTheMoney"],
        contract_size=row["contractSize"],
        currency=row["currency"],
        expiration_date=expiration_date,
        option_type = "call")
    
    calls.append(option)
    


for option in calls:
    print(option)


