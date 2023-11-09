def calculate_tax(price, tax_rate):
    if price < 0:
        raise ValueError("Неверная цена")
    elif tax_rate < 0 or tax_rate >= 100:
        raise ValueError("Неверный налоговый процент")
    total = price + (price * tax_rate / 100)
    return total
