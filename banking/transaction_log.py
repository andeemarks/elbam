from dataclasses import dataclass
from .transaction import Transaction


@dataclass
class TransactionLogEntry:
    account_number: str
    balance: float

    @classmethod
    def from_transaction(cls, transaction: Transaction) -> tuple[TransactionLogEntry, TransactionLogEntry]:
        return (TransactionLogEntry(transaction.from_account_number, -transaction.amount),
                TransactionLogEntry(transaction.to_account_number, transaction.amount))
