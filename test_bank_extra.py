from bank import BankAccount


def test_initial_balance():
    account = BankAccount(500)
    assert account.balance == 500


def test_deposit_returns_new_balance():
    account = BankAccount(100)
    result = account.deposit(50)
    assert result == 150