from banking.transaction import Transaction
from banking.transaction_log import TransactionLog, TransactionLogEntry

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

def test_recognises_credit_and_debit_transactions():
    log = TransactionLog()
    transaction = Transaction("from", "to", 123.45)

    log.add_transaction(transaction)

    assert 2 == len(log.log)

    expected_credit = TransactionLogEntry("from", -123.45)
    expected_debit = TransactionLogEntry("to", 123.45)

    assert expected_debit in log.log
    assert expected_credit in log.log

