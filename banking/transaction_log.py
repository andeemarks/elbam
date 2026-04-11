from dataclasses import dataclass
from .transaction import Transaction


@dataclass
class TransactionLog:
    account_number: str
    balance: float

    @classmethod
    def from_transaction(cls, transaction: Transaction) -> tuple[TransactionLog, TransactionLog]:
        return (TransactionLog(transaction.from_account_number, -transaction.amount),
                TransactionLog(transaction.to_account_number, transaction.amount))
