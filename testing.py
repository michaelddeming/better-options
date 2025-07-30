from classes import Stock
from classes import Option

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
