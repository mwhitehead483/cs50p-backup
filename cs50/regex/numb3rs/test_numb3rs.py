from numb3rs import validate

def test_format():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True

def test_range():
    assert validate("275.3.3.3") == False
    assert validate("1.300.3.3") == False
    assert validate("1.2.400.3") == False
    assert validate("1.2.3.999") == False

def test_bytes_length():
    # Catches buggy code that allows 5-byte IPs
    assert validate("1.2.3.4.5") == False
    # Catches buggy code that only checks the first byte
    assert validate("1.999.999.999") == False

def test_bad_characters():
    assert validate("cat") == False
    assert validate("127.0.0") == False
    assert validate("127.0.0.1.1") == False
    assert validate("1.2.3.for") == False

def test_leading_zeros():
    assert validate("192.00.1.1") == False
    assert validate("1.2.3.01") == False
