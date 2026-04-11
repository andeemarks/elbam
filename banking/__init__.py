from .account import Account
from .account_list import AccountList
from .transaction import Transaction

from typing import List
import logging

logger = logging.getLogger(__name__)


def apply_transactions(opening_accounts: List[dict[str, int]], transactions: List[dict[str, int]]) -> List[Account]:
    accounts = AccountList().add_accounts(opening_accounts).apply(_convert_transactions(transactions))

    return accounts.accounts


def _convert_transactions(transactions: List[dict[str, int]]) -> List[Transaction]:
    return [Transaction(**transaction) for transaction in transactions]  # type: ignore
