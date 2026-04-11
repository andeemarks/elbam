from dataclasses import dataclass, field
from itertools import groupby
from .transaction import Transaction
from .account import Account


@dataclass
class TransactionLogEntry:
    account_number: str
    balance: float


@dataclass
class TransactionLog:
    log: list[TransactionLogEntry] = field(default_factory=list)

    def add_log_entry(self, log_entry: TransactionLogEntry):
        self.log.append(log_entry)

    def add_transaction(self, transaction: Transaction):
        self.log.append(TransactionLogEntry(transaction.from_account_number, -transaction.amount))
        self.log.append(TransactionLogEntry(transaction.to_account_number, transaction.amount))

    def sorted(self) -> TransactionLog:
        sorted_log = sorted(self.log, key=lambda log_entry: log_entry.account_number)

        return TransactionLog(log=sorted_log)

    def aggregate(self) -> list[Account]:
        combined_new_balances: list[Account] = []
        for account_number, balance in groupby(self.sorted().log, key=lambda account: account.account_number):
            total_balance = sum(b.balance for b in balance)
            combined_new_balances.append(Account(account_number, total_balance))

        return combined_new_balances
