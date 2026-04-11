import csv

from banking.account import Account
import banking


def test_full_transactions_happy_path():
    accounts = csv_to_dict_list("./mable_account_balances.csv", ["account_number", "balance"])
    transactions = csv_to_dict_list("./mable_transactions.csv", ["from_account_number", "to_account_number", "amount"])

    updated_accounts = banking.apply_transactions(accounts, transactions)  # type: ignore

    closing_accounts = csv_to_dict_list("./tests/mable_account_balances_expected.csv", ["account_number", "balance"])
    expected_accounts = [Account(**account) for account in closing_accounts]  # type: ignore

    assert sorted(updated_accounts, key=lambda b: b.account_number) == sorted(
        expected_accounts, key=lambda b: b.account_number
    )


def csv_to_dict_list(file_name: str, field_names: list[str]):
    with open(file_name) as csv_file:
        reader = csv.DictReader(csv_file, fieldnames=field_names, skipinitialspace=True, quoting=csv.QUOTE_NONNUMERIC)
        result = [row for row in reader]

    return result
