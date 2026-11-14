from um import count

def test_with_puncuation():
    assert count("um. ;um; UM!") == 3
    assert count("um. ;um; UM!") == 3

def test_with_different_cases():
    assert count("UM um yummy") == 2
    assert count(";um um UM") == 3

def test_with_embedded_um():
    assert count("1.2.3.4.5 um UM yummy") == 2
    assert count("tummy mummmy") == 0
