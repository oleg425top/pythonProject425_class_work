from sys import path

path.append(r'C:\Users\oleg8\PycharmProjects\web_425_modules_packages\modules')

from modules.module import sum_list, product_list
if __name__ == "__main__":
    zero_list = [0 for i in range(5)]
    ones_list = [1 for j in range(5)]
    print(sum_list(zero_list))
    print(product_list(ones_list))

