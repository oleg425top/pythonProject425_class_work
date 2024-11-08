
# def show_quote():
#     name = "Steve Jobs"
#     print('Don\'t let the noise jf other opinions\n'
#           'drown out your own inner voice\n'
#           f'{name.rjust(50)}'
#           )
#
# show_quote()
#
# def count_num(num_1, num_2):
#     if num_1 > num_2:
#         num_1, num_2 = num_2, num_1
#     [print(i, end=' ') if i % 2 != 0 else print('') for i in range(num_1, num_2+1)]
#
# count_num(25,18)


# def draw(lenght,throw,simbol):
#     if throw == "up":
#         for i in range(lenght):
#             print(simbol)
#     elif throw == "front":
#         print(simbol*lenght)
#     else:
#         print('gffgh')

# draw(20,'up','@')
# draw(10,'front','@')

def max_num(a,b,c,d):
    print(f'{max(a, b, c, d)} максимальное число')

max_num(5,65,8,9)