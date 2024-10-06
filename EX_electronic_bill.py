class Bill:
    def __init__(self, client, amount, date):
        self.client = client
        self.amount = amount
        self.date = date
        
    def __str__(self):
        return f"Client: {self.client}, Amount: {self.amount}, Date: {self.date}"
    