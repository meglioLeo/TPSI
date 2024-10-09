from datetime import datetime   #import to get the function to obtain the current date

class Bill:
    def __init__(self, client, amount, date):
        self.client = client
        self.amount = amount
        self.date = date           #format of the date is Y-M-D
        
    def __str__(self):   #return the string representation of the object
        return f"Client: {self.client}, Amount: {self.amount}, Date: {self.date}"
    
    @classmethod 
    def create_daily_bill(cls, client, amount):
        today = datetime.now().date()       #get the current date in the format Y-M-D
        return cls(client, amount, today)
    
bill1 = Bill.create_daily_bill("John", 100)  
print(bill1)  