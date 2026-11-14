import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(3)
    assert(jar.size==3)
    with pytest.raises(ValueError):  #  This would exceed capacity
        jar.deposit(10)
    jar.withdraw(2)
    assert(jar.size==1)

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(3)
    assert jar.size == 7
    # Withdrawing more than current size should raise ValueError
    with pytest.raises(ValueError):
        jar.withdraw(8)

