import csv
import logging

from banking.account import Account
logger = logging.getLogger(__name__)

import banking

def test_full_transactions_happy_path():
    with open("./mable_account_balances.csv") as initial_accounts_file:
        fieldnames = ['account_number', 'balance']
        reader = csv.DictReader(initial_accounts_file, fieldnames=fieldnames, skipinitialspace=True, quoting=csv.QUOTE_NONNUMERIC)
        accounts = [row for row in reader]

    with open("./mable_transactions.csv") as tx_file:
        fieldnames = ['from_account_number', 'to_account_number', 'amount']
        reader = csv.DictReader(tx_file, fieldnames=fieldnames, skipinitialspace=True, quoting=csv.QUOTE_NONNUMERIC)
        transactions = [row for row in reader]

    updated_accounts = banking.apply_transactions(accounts, transactions) # type: ignore

    with open("./tests/mable_account_balances_expected.csv") as closing_balances_file:
        fieldnames = ['account_number', 'balance']
        reader = csv.DictReader(closing_balances_file, fieldnames=fieldnames, skipinitialspace=True, quoting=csv.QUOTE_NONNUMERIC)
        closing_accounts = [row for row in reader]
        expected_accounts = [Account(**account) for account in closing_accounts]
    
    assert sorted(updated_accounts, key=lambda b: b.account_number) == sorted(expected_accounts, key=lambda b: b.account_number)