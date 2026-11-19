from temp_converter import celsius_to_fahrenheit

def test_zero():
    assert celsius_to_fahrenheit(0) == 32

def test_boiling():
    assert celsius_to_fahrenheit(100) == 212

def test_freezing_negative():
    assert celsius_to_fahrenheit(-40) == -40

def test_normal():
    assert celsius_to_fahrenheit(37) == 98.6

def test_25():
    assert celsius_to_fahrenheit(25) == 77