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


@pytest.mark.parametrize("sale, expect", [(0, 110), (10, 99), (100, 0)])
def test_calculate_tax_sale(sale, expect):
    assert calculate_tax(100, 10, sale=sale) == expect


@pytest.mark.parametrize("round_, expect", [(0, 99), (1, 99.4), (2, 99.42), (3, 99.425)])
def test_calculate_tax_round(round_, expect):
    assert calculate_tax(100, 2.5, sale=3, round_=round_) == expect


@pytest.mark.parametrize("price, tax_rate, sale, round_", [("100", 10, 20, 1),
                                                           (100, "10", 20, 1),
                                                           (100, 10, "20", 1),
                                                           (100, 10, 20, "1")
                                                           ])
def test_calculate_tax_check_type(price, tax_rate, sale, round_):
    with pytest.raises(TypeError):
        calculate_tax(price, tax_rate, sale=sale, round_=round_)


def test_calculate_tax_kwargs():
    with pytest.raises(TypeError):
        calculate_tax(100, 10, 5, 2)
