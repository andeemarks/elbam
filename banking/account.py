from dataclasses import dataclass


@dataclass
class Account:
    account_number: int
    balance: float

    def __post_init__(self):
        if self.balance < 0:
            raise ValueError(f"Invalid balance of {self.balance}")

        if len(str(int(self.account_number))) != 16:
            raise ValueError(f"Invalid account number of {self.account_number}")

    def __repr__(self):
        return f"{int(self.account_number)}: {self.balance}"
