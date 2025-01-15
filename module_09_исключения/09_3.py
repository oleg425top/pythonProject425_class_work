def print_args(args):
    lng = len(args)
    if lng == 0:
        print(' ')
    elif lng ==1:
        print(args[0])
    else:
        print(str(args))

try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=':', end=':')
    print_args(e.args)

try:
    raise Exception('my_exeption')
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

try:
    raise Exception('my', 'my_exeption')
except Exception as e:
    print(e, e.__str__(), sep=':', end=':')
    print_args(e.args)

