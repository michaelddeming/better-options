from models.Stock import Stock
from dotenv import load_dotenv
import os



load_dotenv()

key = os.getenv("ALPHA_KEY")

stock = Stock(ticker="tsla")
stock.set_key(key)


# stock.get_insider_transactions()
recent_insider_transactions = stock.recent_insider_transactions(days=31)




