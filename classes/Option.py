
from datetime import datetime


class Option:

    def __init__(self,
                contract_symbol,
                last_trade_date: datetime,
                strike: float,
                last_price: float,
                bid: float,
                ask: float,
                change: float, 
                percent_change: float,
                volume: float,
                open_interest: float,
                implied_volatility: float,
                in_the_money: bool,
                contract_size: str,
                currency: str,
                expiration_date: str,
                option_type: str,
                ):

                # yfinance vars
                self.contract_symbol = contract_symbol
                self.last_trade_date = last_trade_date
                self.strike = strike
                self.last_price = last_price
                self.bid = bid
                self.ask = ask
                self.change = change
                self.percent_change = percent_change
                self.volume = volume
                self.open_interest = open_interest
                self.implied_volatility = implied_volatility
                self.in_the_money = in_the_money
                self.contract_size = contract_size
                self.currency = currency

                # custom vars
                self.expiration_date = expiration_date
                self.option_type = option_type

                # computed instance vars
                self.days_to_expiration = self.compute_days_to_expiration()

                print(f"{self.option_type.title()} succefully generated!")

    def __str__(self):
            return f"{self.contract_symbol}"

    def compute_days_to_expiration(self):
            return (datetime.strptime(self.expiration_date, "%Y-%m-%d") - datetime.today()).days
            
    