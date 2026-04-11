from .account import Account
from .transaction import Transaction
from .transaction_log import TransactionLogEntry, TransactionLog

from pprint import pformat
from typing import List
import logging
logger = logging.getLogger(__name__)


def apply_transactions(accounts: List[dict[str, str]], transactions: List[dict[str, str]]) -> List[Account]:
    opening_balances = seed_balances(accounts)
    transaction_log = record_transactions(convert_transactions(transactions), opening_balances)
    closing_balances = transaction_log.aggregate()

    logger.debug(pformat(closing_balances))

    return closing_balances


def convert_transactions(transactions: List[dict[str, str]]) -> List[Transaction]:
    return [Transaction(**transaction) for transaction in transactions]  # type: ignore


def record_transactions(transactions: List[Transaction],
                        opening_balances: List[Account]) -> TransactionLog:
    transaction_log: TransactionLog = TransactionLog()
    for balance in opening_balances:
        transaction_log.add_log_entry(TransactionLogEntry(balance.account_number, balance.balance))

    for transaction in transactions:
        transaction_log.add_transaction(transaction)

    return transaction_log


def seed_balances(balances: List[dict[str, str]]) -> List[Account]:
    new_balances: List[Account] = []
    for balance in balances:
        new_balances.append(Account(balance['account_number'], float(balance['balance'])))

    return new_balances
