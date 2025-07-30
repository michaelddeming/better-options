from classes.Stock import Stock
from classes.Option import Option


msft = Stock(ticker="MSFT")
expiration_date, msft_calls, msft_puts = msft.get_option_chain(expiration_index=0, export_chain=True)


for option in msft_calls:
    print(option)
