from bank import value

def test_values():
    assert value("hello") == 0
    assert value("Good morning") == 100
    assert value("How are you?") == 20
    assert value("What's up?") == 100
    assert value("Nice dress") == 100
    assert value("Nice shirt") != 0
    assert value("Hola") != 100
