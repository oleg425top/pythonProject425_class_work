# def get_order_total_summ(order_total, country):
#     total = 0
#
#     for items_price in order_total.values():
#         total += items_price[0] * items_price[1]
#
#     if country == 'RU':
#         total += total * 0.2
#     elif country == 'KZ':
#         total += 0.12
#     elif country == 'UAE':
#         total += total * 0.05
#
#     else:
#         return 'Error of country'
#     return total


def get_tax(country):
    if country == 'RU':
        return 0.2
    elif country == 'KZ':
        return 0.12
    elif country == 'UAE':
        return 0.05


def get_order_total_summ(order_total, country):
    total = 0
    for items_price in order_total.values():
        total += items_price[0] * items_price[1]

    if get_tax(country):
        total += total * get_tax(country)
        return total
    else:
        return 'Error of country'




