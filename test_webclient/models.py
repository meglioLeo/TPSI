class TransactionModel:

    def __init__(self, code, enter_place, enter_hour, exit_place, exit_hour, amount):
        self.code = code,
        self.enter_place = enter_place
        self.enter_hour = enter_hour
        self.exit_place = exit_place
        self.exit_hour = exit_hour
        self.amount = amount
    
    @classmethod
    def from_json(cls, data):
        return(
            code = data.get("codice"),
            enter_place = data.get("ingresso"),
            enter_hour = data.get("ora_ingresso"),
            exit_place = data.get("uscita"),
            exit_hour = data.get("ora_uscita"),
            amount = data.get("importo")
        )

    def __repr__(self):
        return f"TransactionModel(code={self.code}, enter_place='{self.enter_place}', enter_hour='{self.enter_hour}', exit_hour='{self.exit_hour}', amount={self.amount})"