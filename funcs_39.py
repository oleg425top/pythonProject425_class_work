# def get_calc_sum(numbers: list):
#     calc_sum = 0
#     for number in numbers:
#         calc_sum += int(number)
#     return calc_sum

'''2 variant'''
def get_calc_sum(list_of_num: list):
    sum_of_list = sum(list(map(int, list_of_num)))
    return sum_of_list

def main():
    numbers_list = input('Введите числа через пробел').split()

    result = get_calc_sum(numbers_list)
    print(result)

main()


