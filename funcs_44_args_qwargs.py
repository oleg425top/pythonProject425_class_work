
'''аналог функции sum'''
def new_sum(*args):
    suma = 0
    for nums in args:
        suma += nums
    return suma

print(new_sum(2,5,8,9,8,8,48,89))

'''Найти самое длинное слово!'''
def longest_word(*args):
    print(args)
    print(type(args))
    leader = ""
    for word in args:
        if type(word) is str:
            if len(word) > len(leader):
                leader = word
    return print(leader)

longest_word('asdasd',5, [], 'asdas')

