import pytest
from src.main import calculate_taxes


@pytest.fixture
def prices():
    return [100, 50, 200]


@pytest.mark.parametrize("tax, expect", [(0, [100, 50, 200]),
                                         (10, [110, 55, 220])
                                         ])
def test_calculate_taxes(prices, tax, expect):
    assert calculate_taxes(prices, tax) == expect


def test_calculate_taxes_invalid_tax(prices):
    with pytest.raises(ValueError):
        calculate_taxes(prices, -3)


def test_calculate_taxes_invalid_price():
    with pytest.raises(ValueError):
        calculate_taxes([-100, 50], 10)
