from classes.Stock import Stock
from classes.Option import Option


msft = Stock(ticker="aapl")
expiration_date, msft_calls, msft_puts = msft.get_option_chain(
    expiration_index=10, export_chain=True, limit=5
)
print("Strike", "Current Price", "Black Scholes", "% Change")
for option in msft_calls:
    bs = round(msft.black_scholes_model(option, 0.0442), 2)
    curr = round(((option.bid + option.ask) / 2), 2)
    change = round(((curr - bs) / bs) * 100, 2)
    print(option.strike, curr, bs, change)

