from dataclasses import dataclass


@dataclass
class Transaction:
    from_account_number: int
    to_account_number: int
    amount: float
