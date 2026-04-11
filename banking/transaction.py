from dataclasses import dataclass


@dataclass
class Transaction:
    from_account_number: int
    to_account_number: int
    amount: float

    def __post_init__(self):
        if len(str(int(self.to_account_number))) != 16:
            raise ValueError(f"Invalid account number of {self.to_account_number}")

        if len(str(int(self.from_account_number))) != 16:
            raise ValueError(f"Invalid account number of {self.from_account_number}")

        if self.from_account_number == self.to_account_number:
            raise ValueError(f"Invalid duplicate account numbers of {self.from_account_number}")
