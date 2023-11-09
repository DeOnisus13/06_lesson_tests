import pytest
from src.work_2 import calculate_tax


@pytest.mark.parametrize("price, tax_rate, expect", [(100, 10, 110), (50, 5, 52.5)])
def test_calculate_tax(price, tax_rate, expect):
    assert calculate_tax(price, tax_rate) == expect


def test_calculate_tax_incorrect():
    with pytest.raises(ValueError):
        calculate_tax(-100, 10)
    with pytest.raises(ValueError):
        calculate_tax(100, -3)
