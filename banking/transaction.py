from dataclasses import dataclass


@dataclass
class Transaction:
    from_account_number: str
    to_account_number: str
    amount: float
