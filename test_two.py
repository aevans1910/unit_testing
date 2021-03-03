import math
import pytest

T_HALF = 5730
DECAY_CONSTANT = -0.693

def get_age_carbon_14_dating(carbon_14_ratio):
    """Returns the estimated age of the sample in year.
    carbon_14_ratio: the percent (0 < percent < 1) of carbon-14 
    in the sample conpared to the amount in living 
    tissue (unitless). 
    """
    if carbon_14_ratio <= 0 or carbon_14_ratio >= 1:
        raise TypeError('Carbon_14_ratio must be within the range of 0 < percentage < 1')

    return math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF 

def test_average_input():
    assert get_age_carbon_14_dating(0.35) == 8680.34743633106

def test_input_zero():
    with pytest.raises(TypeError):
        get_age_carbon_14_dating(0)

def test_input_one():
    with pytest.raises(TypeError):
        get_age_carbon_14_dating(1)

def test_input_negative():
    with pytest.raises(TypeError):
        get_age_carbon_14_dating(-2)

def test_string_input():
    with pytest.raises(TypeError):
        get_age_carbon_14_dating('0.35')

class InsufficientAmount(Exception):
    pass


class Wallet(object):

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount

@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(20)

def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
    assert wallet.balance == 20

def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100

def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)
