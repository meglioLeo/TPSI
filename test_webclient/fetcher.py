import requests
from config import URL
from models import TransactionModel
import xml.etree.ElementTree as ET
from datetime import datetime 

class TransactionFetcher:
    def __init__(self, url=URL):
        self.url = url

    def fetch_transactions(self):
        response = requests.get(self.url)
        response.raise_for_status

        root = ET.fromstring(response.text)
        transactions = []

        for transaction in root.findall("transazione"):
            transactions.append(Transaction(
                code = int(transaction.find("codice").text)),
                enter_place = transaction.find("ingresso").text,
                enter_hour = datetime.fromisoformat(transaction.find("ora_ingresso").text),
                exit_place = transaction.find("uscita").text,
                exit_hour = datetime.fromisoformat(transaction.find("ora_uscita").text),
                amount = int(transaction.find("importo").text)
            )

        return transactions