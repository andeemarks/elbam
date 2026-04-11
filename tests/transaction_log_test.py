from banking.account import Account
from banking.transaction import Transaction
from banking.transaction_log import TransactionLog, TransactionLogEntry

import pytest


def test_empty_on_creation():
    log = TransactionLog()

    assert 0 == len(log.log)


def test_contains_log_entries():
    log = TransactionLog()
    log_entry = TransactionLogEntry(1111234522226789, 124.56)

    log.add_account(log_entry)

    assert 1 == len(log.log)
    assert log.log[0] == log_entry

    log_entry = TransactionLogEntry(1111234522221234, 567.89)

    log.add_account(log_entry)

    assert 2 == len(log.log)
    assert log.log[1] == log_entry


def test_splits_transaction_into_credit_and_debit():
    log = TransactionLog()

    log.add_account(TransactionLogEntry(1111234522226789, 200))
    log.add_account(TransactionLogEntry(1111234522221234, 200))
    log.add_transaction(Transaction(1111234522226789, 1111234522221234, 123.45))

    assert 4 == len(log.log)

    expected_credit = TransactionLogEntry(1111234522226789, -123.45)
    expected_debit = TransactionLogEntry(1111234522221234, 123.45)

    assert expected_debit in log.log
    assert expected_credit in log.log


def test_reconciles_balances_within_accounts():
    log = TransactionLog()

    log.add_account(TransactionLogEntry(1111234522226789, 500))
    log.add_account(TransactionLogEntry(1111234522221234, 600))
    log.add_transaction(Transaction(1111234522226789, 1111234522221234, 123.45))
    log.add_transaction(Transaction(1111234522221234, 1111234522226789, 67.89))

    result = log.reconcile()

    assert 2 == len(result)
    assert Account(1111234522226789, 500 - 123.45 + 67.89) in result
    assert Account(1111234522221234, 600 + 123.45 - 67.89) in result


def test_cannot_add_transaction_if_insufficient_funds():
    log = TransactionLog()
    transaction = Transaction(1111234522226789, 1111234522221234, 123.45)

    with pytest.raises(ValueError):  # type: ignore
        log.add_transaction(transaction)
