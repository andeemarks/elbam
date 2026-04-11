from .account import Account, AccountList
from .transaction import Transaction
from .transaction_log import TransactionLogEntry, TransactionLog

from pprint import pformat
from typing import List
import logging
logger = logging.getLogger(__name__)


def apply_transactions(accounts: List[dict[str, int]], transactions: List[dict[str, int]]) -> List[Account]:
    opening_balances = AccountList()
    opening_balances.add_accounts(accounts)

    transaction_log = record_transactions(convert_transactions(transactions), opening_balances)
    closing_balances = transaction_log.aggregate()

    logger.debug(pformat(closing_balances))

    return closing_balances


def convert_transactions(transactions: List[dict[str, int]]) -> List[Transaction]:
    return [Transaction(**transaction) for transaction in transactions]  # type: ignore


def record_transactions(transactions: List[Transaction],
                        accounts: AccountList) -> TransactionLog:
    transaction_log: TransactionLog = TransactionLog()
    for account in accounts.accounts:
        transaction_log.add_log_entry(TransactionLogEntry(account.account_number, account.balance))

    for transaction in transactions:
        transaction_log.add_transaction(transaction)

    return transaction_log
