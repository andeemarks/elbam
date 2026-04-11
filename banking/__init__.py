from .account import Account
from .transaction_processor import TransactionProcessor

from typing import List
import logging

logger = logging.getLogger(__name__)


def apply_transactions(opening_accounts: List[dict[str, int]], transactions: List[dict[str, int]]) -> List[Account]:
    processor = TransactionProcessor(raw_accounts=opening_accounts, raw_transactions=transactions)

    return processor.accounts
