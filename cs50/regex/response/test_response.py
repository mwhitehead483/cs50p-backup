from response import is_valid_email

def test_valid_email():
    assert is_valid_email("test@example.com") == True
    assert is_valid_email("user.name+tag@sub.domain.co.uk") == True
    assert is_valid_email("malan@harvard.edu") is True

def test_invalid_email():
    assert is_valid_email("plainaddress") == False
    assert is_valid_email("@missingusername.com") == False
    assert is_valid_email("username@.com") == False
    assert is_valid_email("") == False
    assert is_valid_email("malan@@@harvard.edu") is False
    assert is_valid_email("@harvard.edu") is False
    assert is_valid_email("malan@.edu") is False
