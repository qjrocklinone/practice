from mathclubs import *

def test_factorial():
    assert fact(1) == 1
    assert fact(2) == 2
    assert fact(6) == 6 * 5 * 4 * 3 * 2 * 1


def test_nchoosek():
    assert choose(5, 1) == 5
    assert choose(5, 2) == 10
    assert choose(5, 5) == 1
