def get_sum_tax(value, tax_percent):
    total = value + value * tax_percent / 100
    return total

may_total = get_sum_tax(10000, 13)
print(may_total)
print(get_sum_tax(10000, 13))

my_sum = 15000
my_tax = 9
my_total_sum = get_sum_tax(my_sum, my_tax)
print(f"налог {my_tax} процентов от {my_sum} равен {my_total_sum} рублей")