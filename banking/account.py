from dataclasses import dataclass


@dataclass
class Account:
    account_number: int
    balance: float

    def __post_init__(self):
        self.account_number = int(self.account_number)

        if self.balance < 0:
            raise ValueError(f"Invalid balance of {self.balance}")

        if len(str(self.account_number)) != 16:
            raise ValueError(f"Invalid account number of {self.account_number}")

    def __repr__(self):
        return f"{self.account_number}: {self.balance}"
