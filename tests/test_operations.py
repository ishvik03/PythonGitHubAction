from src.math_operations import  add, subtract

def test_add():

    assert add(1, 2) == 3
    assert add(5, 6) == 11
    assert add(1, 2) == 3
    assert add(5, 6) == 11

def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(5, 6) == 0
    assert subtract(1, 2) == 1
    assert subtract(5, 6) == 0