import pytest

from banking.transaction import Transaction

def test_holds_account_numbers_and_amount():
    transaction = Transaction(1111234522226789, 1212343433335665, 123.45)

    assert 1111234522226789 == transaction.from_account_number
    assert 1212343433335665 == transaction.to_account_number
    assert 123.45 == transaction.amount

def test_account_numbers_must_be_16_digits():
    with pytest.raises(ValueError):
        Transaction(0, 1212343433335665, 123.45)

    with pytest.raises(ValueError):
        Transaction(1212343433335665, 0, 123.45)
        
    with pytest.raises(ValueError):
        Transaction(12345678901234567, 0, 123.45)

    with pytest.raises(ValueError):
        Transaction(0, 12345678901234567, 123.45)

def test_transactions_cannot_be_to_same_account():
    with pytest.raises(ValueError):
        Transaction(1111234522226789, 1111234522226789, 123.45)
