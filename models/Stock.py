import json
import requests
import os




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