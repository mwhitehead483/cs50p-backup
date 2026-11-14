from twttr import shorten

def test_lower_vowels():
    assert shorten("twitter") == "twttr"

def test_upper_vowels():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("AEIOU") == ""

def test_numbers():
    assert shorten("CS50") == "CS50"

def test_punctuation():
    assert shorten("What's your name?") == "Wht's yr nm?"
