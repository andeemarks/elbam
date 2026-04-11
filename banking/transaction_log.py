from dataclasses import dataclass


@dataclass
class TransactionLog:
    account_number: str
    balance: float
