from banking.account import Account
from banking.transaction import Transaction
from banking.transaction_log import TransactionLog, TransactionLogEntry

import pytest

def test_empty_on_creation():
    log = TransactionLog()

    assert 0 == len(log.log)

def test_contains_log_entries():
    log = TransactionLog()
    log_entry = TransactionLogEntry("account1", 124.56)

    log.add_log_entry(log_entry)

    assert 1 == len(log.log)
    assert log.log[0] == log_entry
    
    log_entry = TransactionLogEntry("account2", 567.89)

    log.add_log_entry(log_entry)

    assert 2 == len(log.log)
    assert log.log[1] == log_entry

def test_splits_transaction_into_credit_and_debit():
    log = TransactionLog()

    log.add_log_entry(TransactionLogEntry("from", 200))
    log.add_log_entry(TransactionLogEntry("to", 200))
    log.add_transaction(Transaction("from", "to", 123.45))

    assert 4 == len(log.log)

    expected_credit = TransactionLogEntry("from", -123.45)
    expected_debit = TransactionLogEntry("to", 123.45)

    assert expected_debit in log.log
    assert expected_credit in log.log

def test_aggregates_balances_within_accounts():
    log = TransactionLog()

    log.add_log_entry(TransactionLogEntry("from", 500))
    log.add_log_entry(TransactionLogEntry("to", 600))
    log.add_transaction(Transaction("from", "to", 123.45))
    log.add_transaction(Transaction("to", "from", 67.89))

    result = log.aggregate()

    assert 2 == len(result)
    assert Account("from", 500 - 123.45 + 67.89) in result
    assert Account("to", 600 + 123.45 - 67.89) in result

def test_cannot_add_transaction_if_insufficient_funds():
    log = TransactionLog()
    transaction = Transaction("from", "to", 123.45)

    with pytest.raises(ValueError):  # type: ignore
        log.add_transaction(transaction)
