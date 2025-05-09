def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def divide(a, b):
    return a / b
    

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0.3, 0.7) == 1


def test_resta():
    assert resta(5, 2) == 3
    assert resta(1, 1) == 1

def test_multiplication():
    assert multiplication(3,3) == 9
    assert multiplication(2,5) == 10

def test_divide():
    assert divide(12,3) == 4
    assert divide(20,4) == 5



