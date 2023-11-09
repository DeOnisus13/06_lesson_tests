def calculate_tax(price, tax_rate, *, sale=0, round_=2):

    for arg in (price, tax_rate, sale, round_):
        if not isinstance(arg, (int, float)):
            raise TypeError("Это не число")

    if price < 0:
        raise ValueError("Неверная цена")

    elif tax_rate < 0 or tax_rate >= 100:
        raise ValueError("Неверный налоговый процент")

    tax = price * tax_rate / 100
    total = price + tax
    total_sale = total - (total * sale / 100)
    return round(total_sale, round_)
