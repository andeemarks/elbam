from pprint import pformat
from itertools import groupby
from typing import List
import logging
logger = logging.getLogger(__name__)


def apply_transactions(balances: List[dict[str, str]], transactions: List[dict[str, str]]) -> List[dict[str, float]]:
    new_balances = seed_balances(balances)
    new_balances = record_transactions(balances, transactions, new_balances)
    new_balances = sorted(new_balances, key=lambda b: b['account_number'])

    logger.debug(pformat(new_balances))
    closing_balances = aggregate_transactions_across_accounts(new_balances)

    logger.debug(pformat(closing_balances))

    return closing_balances


def aggregate_transactions_across_accounts(new_balances: List[dict[str, float]]):
    combined_new_balances: List[dict[str, float]] = []
    for account_number, balance in groupby(new_balances, key=lambda b: b['account_number']):
        # logger.debug(account_number)
        # logger.debug(pformat(list(balance)))
        total_balance = sum(b['balance'] for b in balance)
        # logger.debug(total_balance)
        combined_new_balances.append({'account_number': account_number, 'balance': total_balance})

    return combined_new_balances


def record_transactions(balances: List[dict[str, str]],
                        transactions: List[dict[str, str]],
                        new_balances: List[dict[str, float]]) -> List[dict[str, float]]:
    for transaction in transactions:
        from_account_number = transaction['from_account_number']
        to_account_number = transaction['to_account_number']
        amount = float(transaction['amount'])
        from_account = next((b for b in balances if b.get('account_number') == from_account_number))
        to_account = next((b for b in balances if b.get('account_number') == to_account_number))
        new_balances.append({'account_number': from_account['account_number'], 'balance': -amount})
        new_balances.append({'account_number': to_account['account_number'], 'balance': amount})

    return new_balances


def seed_balances(balances: List[dict[str, str]]) -> List[dict[str, float]]:
    new_balances: List[dict[str, float]] = []
    for balance in balances:
        new_balances.append({'account_number': balance['account_number'], 'balance': float(balance['balance'])})

    return new_balances
