import pytest
from wallet import Wallet


def test_default_initial_amount(): #we wanna verify that the default amount is zero
    wallet = Wallet()
    assert wallet.balance == 0

@pytest.mark.parametrize("what_was_inserted, what_is_expected", [(-34,-34),(900,90),(32,32),(666, 6666)])
def test_setting_initial_amount(what_was_inserted, what_is_expected): #we are testing if the default amount is the same as the amount we set is correct
    wallet = Wallet(what_was_inserted) #we are setting the default amount to a value immediately an object of the class  is created
    assert wallet.balance ==what_is_expected


@pytest.mark.parametrize("original_balance, added_cash,expected_balance",[(1,11,12),(2,22,24),(3,35,0),(40,44,84)])
def test_wallet_add_cash(original_balance,added_cash,expected_balance):#we are trying to see if the add cash method will add up the initial amount to the new value we wanna add
    wallet = Wallet(original_balance)
    wallet.add_cash(added_cash)
    assert wallet.balance == expected_balance #checkin the new balance if it talies, i.e whther the function worked correctly

@pytest.mark.parametrize("original_balance, spent_cash, expected_balance",[(100,11,89),(23,22,0),(65,35,30),(100,44,44)])
def test_wallet_spend_cash(original_balance, spent_cash,expected_balance):
    wallet = Wallet(original_balance)
    wallet.spend_cash(spent_cash)
    assert wallet.balance ==expected_balance

