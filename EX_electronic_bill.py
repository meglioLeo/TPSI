from datetime import datetime   #import to get the function to obtain the current date

class Bill:
    def __init__(self, client, amount, date):
        self.client = client
        self.amount = amount
        self.date = date
        
    def __str__(self):
        return f"Client: {self.client}, Amount: {self.amount}, Date: {self.date}"
    
    @classmethod #Todo
    def create_daily_bill(cls, client, amount):
        today = datetime.date.now()
        return cls(client, amount, today)
    
bill1 = Bill.create_daily_bill("John", 100)  #create a bill for John with an amount of 100
print(bill1)  #print the bill