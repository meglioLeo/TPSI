class TransactionModel:

    def __init__(self, code, enter_place, enter_hour, exit_place, exit_hour, amount):
        self.code = code,
        self.enter_place = enter_place
        self.enter_hour = enter_hour
        self.exit_place = exit_place
        self.exit_hour = exit_hour
        self.amount = amount

    def __repr__(self):
        return f"TransactionModel(code={self.code}, enter_place='{self.enter_place}', enter_hour='{self.enter_hour}', exit_hour='{self.exit_hour}', amount={self.amount})"