import pytest
from src.divide import divide

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)