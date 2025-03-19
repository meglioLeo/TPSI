from fetcher import TransactionFetcher
from filter import count_enter_Livorno
from filter import amount_spent_in_year
#from filter import total_time
from datetime import datetime

def main():
    fetcher = TransactionFetcher()
    transactions = fetcher.fetch_transactions
    if not transactions:
        print("No users found or URL request failed.")
        return
    
    n_times_enter_livorno = count_enter_Livorno(transactions)
    print(f"User entered from Livorno "{n_times_enter_livorno}" times")

    amount_spent = amount_spent_in_year(transactions)
    print(f"User spent in total "{amount_spent}" euro")

if __name__=="__main__":
    main()