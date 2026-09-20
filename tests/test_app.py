from calculator.app import add

def test_add_positive_integers():
    """Verify standard addition handles baseline integers."""
    assert add(4, 5) == 9

def test_add_negative_integers():
    """Verify calculation engine correctly computes signed numbers."""
    assert add(-2, -8) == -10

def test_add_zero_identity():
    """Verify that adding zero returns the baseline value."""
    assert add(7, 0) == 7
