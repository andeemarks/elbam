import csv
import logging
logger = logging.getLogger(__name__)
from pprint import pformat

import banking

def test_full_transactions_happy_path():
    with open("./mable_account_balances.csv") as opening_balances_file:
        fieldnames = ['account_number', 'balance']
        reader = csv.DictReader(opening_balances_file, fieldnames=fieldnames, skipinitialspace=True, quoting=csv.QUOTE_NONNUMERIC)
        opening_balances = [row for row in reader]
        logging.debug(pformat(opening_balances))

    with open("./tests/mable_account_balances_expected.csv") as closing_balances_file:
        fieldnames = ['account_number', 'balance']
        reader = csv.DictReader(closing_balances_file, fieldnames=fieldnames, skipinitialspace=True, quoting=csv.QUOTE_NONNUMERIC)
        closing_balances = [row for row in reader]
        logging.debug(pformat(closing_balances))

    with open("./mable_transactions.csv") as tx_file:
        fieldnames = ['from_account_number', 'to_account_number', 'amount']
        reader = csv.DictReader(tx_file, fieldnames=fieldnames, skipinitialspace=True, quoting=csv.QUOTE_NONNUMERIC)
        transactions = [row for row in reader]
        logging.debug(pformat(transactions))

    updated_balances = banking.apply_transactions(opening_balances, transactions) # type: ignore
    logging.debug(pformat(updated_balances))
    
    assert sorted(updated_balances, key=lambda b: b['account_number']) == sorted(closing_balances, key=lambda b: b['account_number'])