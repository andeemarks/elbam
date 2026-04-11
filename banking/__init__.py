from .account import Account
from .transaction import Transaction
from .transaction_log import TransactionLog

from pprint import pformat
from itertools import groupby
from typing import List
import logging
logger = logging.getLogger(__name__)


def apply_transactions(balances: List[dict[str, str]], transactions: List[dict[str, str]]) -> List[Account]:
    opening_balances = seed_balances(balances)
    transaction_log = record_transactions(convert_transactions(transactions), opening_balances)
    transaction_log = sorted(transaction_log, key=lambda account: account.account_number)

    # logger.info(pformat(transaction_log))
    closing_balances = aggregate_transactions_across_accounts(transaction_log)

    logger.debug(pformat(closing_balances))

    return closing_balances


def convert_transactions(transactions: List[dict[str, str]]) -> List[Transaction]:
    return [Transaction(**transaction) for transaction in transactions]


def aggregate_transactions_across_accounts(transaction_log: List[TransactionLog]) -> List[Account]:
    combined_new_balances: List[Account] = []
    for account_number, balance in groupby(transaction_log, key=lambda account: account.account_number):
        total_balance = sum(b.balance for b in balance)
        combined_new_balances.append(Account(account_number, total_balance))

    return combined_new_balances


def record_transactions(transactions: List[Transaction],
                        opening_balances: List[Account]) -> List[TransactionLog]:
    transaction_log: List[TransactionLog] = []
    for balance in opening_balances:
        transaction_log.append(TransactionLog(balance.account_number, balance.balance))

    for transaction in transactions:
        from_account_number = transaction.from_account_number
        to_account_number = transaction.to_account_number
        amount = transaction.amount
        from_account = next((b for b in opening_balances if b.account_number == from_account_number))
        to_account = next((b for b in opening_balances if b.account_number == to_account_number))
        transaction_log.append(TransactionLog(from_account.account_number, -amount))
        transaction_log.append(TransactionLog(to_account.account_number, amount))

    return transaction_log


def seed_balances(balances: List[dict[str, str]]) -> List[Account]:
    new_balances: List[Account] = []
    for balance in balances:
        new_balances.append(Account(balance['account_number'], float(balance['balance'])))

    return new_balances
