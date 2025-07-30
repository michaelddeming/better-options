
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
                ):
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
        