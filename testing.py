from classes.Stock import Stock
from classes.Option import Option


msft = Stock(ticker="MSFT")
expiration_date, msft_calls, msft_puts = msft.get_option_chain(expiration_index=0, export_chain=True)

prices = []
for option in msft_calls:
    bs = round(msft.black_scholes_model(option, .0442), 2)
    curr = round(((option.bid + option.ask) / 2), 2)
    change = round(((bs - curr) / curr) * 100, 2) 
    prices.append((option.strike,curr, bs, change))

print(prices)

