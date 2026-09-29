def test_shared_1(funded_account):
    assert funded_account.balance == 1000

def test_shared_2(funded_account):
    funded_account.deposit(100)
    assert funded_account.balance == 1100