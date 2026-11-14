from plates import is_valid

def test_min_max_length():
    assert is_valid("AB") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFGH") == False
    assert is_valid("") == False

def test_start_with_two_letters():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("C50") == False

def test_number_placement():
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False  # First number cannot be '0'

def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("CS-50") == False
    assert is_valid("HELLO, WORLD") == False
