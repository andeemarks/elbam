
from dataclasses import dataclass, field
from typing import List

from banking.account import Account
from banking.transaction import Transaction
from banking.transaction_log import TransactionLog, TransactionLogEntry


@dataclass
class AccountList:
    accounts: List[Account] = field(default_factory=list)  # type: ignore

    def add_accounts(self, accounts: List[dict[str, int]]) -> AccountList:
        for account in accounts:
            self.accounts.append(Account(account['account_number'], float(account['balance'])))

        return self

    def apply(self, transactions: List[Transaction]) -> AccountList:
        transaction_log = self._record_transactions(transactions)

        self.accounts = transaction_log.aggregate()

        return self

    def _record_transactions(self, transactions: List[Transaction]) -> TransactionLog:
        transaction_log: TransactionLog = TransactionLog()
        for account in self.accounts:
            transaction_log.add_log_entry(TransactionLogEntry(account.account_number, account.balance))

        for transaction in transactions:
            transaction_log.add_transaction(transaction)

        return transaction_log
