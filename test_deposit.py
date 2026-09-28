import pytest
from bank import BankAccount

@pytest.fixture
def account():
    return BankAccount(100)

def test_deposit_50(account):
    account.deposit(50)
    assert account.balance == 150

def test_deposit_100(account):
    account.deposit(100)
    assert account.balance == 200