import json
import requests
import os
import datetime
from models.InsiderTransaction import InsiderTransaction




class Stock:

    def __init__(self, ticker: str, key: str=None):

        self._ticker = ticker.lower()
        self.key = key

    def get_insider_transactions(self):
        if self.key is None:
            raise ValueError("No API key assiged to class.")
        url = f'https://www.alphavantage.co/query?function=INSIDER_TRANSACTIONS&symbol={self.ticker.upper()}&apikey={self.key}'
        r = requests.get(url)
        data = r.json()

        self.write_response_json(data, "insider_transactions")
        return data



    def set_key(self, key:str):
        self.key = key

    @property
    def ticker(self):
        return self._ticker
    
    

    def write_response_json(self, response: json, title: str):

        dir_path = os.path.join("data", self.ticker)
        os.makedirs(dir_path, exist_ok=True)


        file_path = os.path.join(dir_path, f"{title}_{self.ticker}.json")

        with open(file_path, "w") as file:
            json.dump(response, file, indent=2)

    def recent_insider_transactions(self, days: int):

        with open(f"data/{self.ticker}/insider_transactions_{self.ticker}.json", "r") as file:
            found_recent = []
            insider_transactions = json.load(file)
            today = datetime.datetime.today().date()
            for insider_transaction in insider_transactions["data"]:
                transaction_date = insider_transaction["transaction_date"]
                transaction_date = datetime.datetime.strptime(transaction_date, "%Y-%m-%d").date()
                delta = (today - transaction_date).days
                if delta <= days:
                    found_recent.append(insider_transaction)

            if found_recent:
                print(f"\nFound {len(found_recent)} Insider {self.ticker.upper()} Transactions (<=31 Days)")
                sold_cost = 0
                shares_sold = 0

                shares_acq = 0
                acq_cost = 0

                for recent_insider_transaction in found_recent:

                    transaction = InsiderTransaction(**recent_insider_transaction)
                    if transaction.acquisition_or_disposal == "D":
                        shares_sold += transaction.shares
                        sold_cost += (transaction.shares * transaction.share_price)
                    else:
                        shares_acq += transaction.shares
                        acq_cost += (transaction.shares * transaction.share_price)

                sold_avg = sold_cost / shares_sold if shares_sold else 0
                acq_avg = acq_cost / shares_acq if shares_acq else 0

                print(f"\nSold: {shares_sold:.2f} @ ~${sold_avg:.2f}")
                print(f"\nAcquired: {shares_acq:.2f} @ ~${acq_avg:.2f}")

                delta = shares_acq - shares_sold

                if delta > 0:
                    print(f"\nPositive {delta:.2f} Net Change for {self.ticker.upper()} Insider Transactions in {days} Days.")
                elif delta < 0:
                    print(f"\nNegative {delta:.2f} Net Change for {self.ticker.upper()} Insider Transactions in {days} Days.")
                else:
                    print(f"\n{delta:.2f} Net Change for {self.ticker.upper()} Insider Transactions in {days} Days.")
            else:
                print(f"\nFound 0 Insider Transactions (<=31 Days)")
                