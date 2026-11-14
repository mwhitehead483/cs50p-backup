import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("0/4") == 0

def test_convert_valueserror():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("3/2")  # X cannot be greater than Y
    with pytest.raises(ValueError):
        convert("-1/2")  # Fraction cannot be negative

def test_convert_zerodivisionerror():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
