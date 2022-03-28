import calculator
def test_add():
    x=2
    y=6
    result = calculator.add(x,y)
    assert  result==x+y


def test_sub():
    x = 2
    y = 6
    result = calculator.sub(x, y)
    assert result == x - y


def test_mul():
    x = 2
    y = 6
    result = calculator.mul(x, y)
    assert result == x*y


def test_div():
    x = 2
    y = 6
    result = calculator.div(x, y)
    assert result == x / y

