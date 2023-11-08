import pytest
from src.main import calculate_taxes

# @pytest.mark.parametrize("price, tax, expect", [(100, 10, 110), (50, 5, 52.5)])
# def test_calculate_taxes(price, tax, expect):
#     assert calculate_taxes(price, tax) == expect


@pytest.fixture
def coll():
    return [100, 50, 200], 10


def test_calculate_taxes(coll):
    assert calculate_taxes(coll) == [110, 55, 220]
