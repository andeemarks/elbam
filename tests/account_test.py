import pytest

from banking.account import Account

def test_holds_account_number_and_balance():
    account = Account(1111234522226789, 123.45)

    assert 1111234522226789 == account.account_number
    assert 123.45 == account.balance

def test_balances_must_be_positive():
    account = Account(1111234522226789, 0)

    assert 0 == account.balance

    with pytest.raises(ValueError):    
        Account(1111234522226789, -1)

def test_account_number_must_be_16_digits():
    with pytest.raises(ValueError):
        Account(0, 0)
        
    with pytest.raises(ValueError):
        Account(12345678901234567, 0)
