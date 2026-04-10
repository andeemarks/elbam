import csv
import logging
logger = logging.getLogger(__name__)
from pprint import pformat

import banking

def test_full_transactions_happy_path():
    with open("./mable_account_balances.csv") as balances_file:
        fieldnames = ['account_number', 'balance']
        reader = csv.DictReader(balances_file, fieldnames=fieldnames)
        balances = [row for row in reader]
        logging.info(pformat(balances))

    with open("./mable_transactions.csv") as tx_file:
        fieldnames = ['from_account_number', 'to_account_number', 'amount']
        reader = csv.DictReader(tx_file, fieldnames=fieldnames)
        transactions = [row for row in reader]
        logging.info(pformat(transactions))

    updated_balances = banking.apply_transactions(balances, transactions) # type: ignore
    
    assert updated_balances is not None