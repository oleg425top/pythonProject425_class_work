def print_ex_tree(this_class, nest=0):
    if nest >= 1:
        print('|' * (nest - 1), end='')
    if nest > 0:
        print('+----', end='')
    print(this_class.__name__)

    for subclass in this_class.__subclasses__():
        print_ex_tree(subclass, nest + 1)


print_ex_tree(BaseException)
