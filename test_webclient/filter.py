from datetime import datetime

def count_enter_Livorno(transactions):
    return sum(1 for transaction in transactions if transaction.enter_place == "Livrono")

def amount_spent_in_year(transactions):
    return sum(transaction.amount for transaction in transactions)