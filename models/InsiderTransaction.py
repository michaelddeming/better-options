import datetime

class InsiderTransaction:

    def __init__(self,
                 transaction_date: datetime.date,
                 ticker: str,
                 executive: str,
                 executive_title: str,
                 security_type: str,
                 acquisition_or_disposal: str,
                 shares: float,
                 share_price: float):
        
        self.transaction_date = datetime.datetime.strptime(transaction_date, "%Y-%m-%d").date()
        self.ticker = ticker
        self.executive = executive
        self.executive_title = executive_title
        self.security_type = security_type
        self.acquisition_or_disposal = acquisition_or_disposal
        self.shares = float(shares)
        self.share_price = float(share_price)