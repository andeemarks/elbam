# elbam

Applies a list of transactions to a set of opening account balances and returns the closing balances.

## Install

```bash
pip install flake8 flake8-pyproject pytest pytest-cov
```

## Lint

```bash
flake8 .
```

## Test

```bash
pytest
```

## Run

```bash
python -m banking [balances.csv] [transactions.csv]
```

Defaults to `./mable_account_balances.csv` and `./mable_transactions.csv`.

CSV formats:

```
# balances.csv
account_number,balance

# transactions.csv
from_account_number,to_account_number,amount
```

## How it works

```mermaid
sequenceDiagram
    participant M as __main__
    participant I as banking/__init__
    participant AL as AccountList
    participant TL as TransactionLog

    M->>M: read CSVs into dicts
    M->>I: apply_transactions(accounts, transactions)
    I->>AL: AccountList().add_accounts(accounts)
    AL->>AL: create Account per row
    I->>I: convert_transactions(transactions)
    I->>I: create Transaction per row
    I->>AL: .apply(transactions)
    AL->>TL: TransactionLog()
    AL->>TL: add_log_entry() per Account
    AL->>TL: add_transaction() per Transaction
    TL->>TL: append debit + credit entries
    AL->>TL: aggregate()
    TL->>TL: sort by account_number
    TL->>TL: sum balances per account
    TL-->>AL: List[Account]
    AL-->>I: AccountList
    I-->>M: List[Account]
    M->>M: log closing balances
```
