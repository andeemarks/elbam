from typing import List
from banking import apply_transactions
from banking.account import Account
from pprint import pformat

import sys
import csv
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')


def main() -> int:
    balances_file = sys.argv[1] if len(sys.argv) > 1 else "./mable_account_balances.csv"
    transactions_file = sys.argv[2] if len(sys.argv) > 2 else "./mable_transactions.csv"

    closing_balances = _run(balances_file, transactions_file)

    logger.info("CLOSING BALANCES")
    logger.info(pformat(closing_balances))

    return 0


def _run(balances_file: str, transactions_file: str) -> List[Account]:
    balances = _csv_to_dict_list(balances_file, ['account_number', 'balance'])
    logger.info("OPENING BALANCES")
    logger.info(pformat(balances))

    transactions = _csv_to_dict_list(transactions_file, ['from_account_number', 'to_account_number', 'amount'])
    logger.info("TRANSACTIONS")
    logger.info(pformat(transactions))

    return apply_transactions(balances, transactions)


def _csv_to_dict_list(file_name: str, field_names: list[str]) -> list[dict[str, int]]:
    with open(file_name) as csv_file:
        reader = csv.DictReader(csv_file, fieldnames=field_names, skipinitialspace=True, quoting=csv.QUOTE_NONNUMERIC)
        result = [row for row in reader]

    return result  # type: ignore


if __name__ == '__main__':
    sys.exit(main())
