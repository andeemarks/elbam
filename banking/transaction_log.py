from dataclasses import dataclass, field
from itertools import groupby
from .transaction import Transaction
from .account import Account


@dataclass
class TransactionLogEntry:
    account_number: int
    balance: float


@dataclass
class TransactionLog:
    log: list[TransactionLogEntry] = field(default_factory=list)  # type: ignore

    def add_log_entry(self, log_entry: TransactionLogEntry):
        self.log.append(log_entry)

    def add_transaction(self, transaction: Transaction):
        self.add_log_entry(TransactionLogEntry(transaction.from_account_number, -transaction.amount))
        self.add_log_entry(TransactionLogEntry(transaction.to_account_number, transaction.amount))

        self.aggregate()

    def _sorted(self) -> TransactionLog:
        sorted_log = sorted(self.log, key=lambda log_entry: log_entry.account_number)

        return TransactionLog(log=sorted_log)

    def aggregate(self) -> list[Account]:
        combined_new_balances: list[Account] = []
        for account_number, balance in groupby(self._sorted().log, key=lambda account: account.account_number):
            total_balance = sum(b.balance for b in balance)

            if total_balance < 0:
                raise ValueError(f"Invalid balance of {total_balance} for account {account_number}")

            combined_new_balances.append(Account(account_number, total_balance))

        return combined_new_balances
