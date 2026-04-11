from .account import Account
from .account_list import AccountList
from .transaction import Transaction

from typing import List
import logging
logger = logging.getLogger(__name__)


def apply_transactions(accounts: List[dict[str, int]], transactions: List[dict[str, int]]) -> List[Account]:
    opening_balances = AccountList()
    opening_balances.add_accounts(accounts)

    closing_balances = opening_balances.apply_transactions(convert_transactions(transactions))

    return closing_balances


def convert_transactions(transactions: List[dict[str, int]]) -> List[Transaction]:
    return [Transaction(**transaction) for transaction in transactions]  # type: ignore
