class MyZeroDivision(ZeroDivisionError):
    pass


def do_zero_division(mine):
    if mine:
        raise MyZeroDivision('Очень плохие новости')
    else:
        raise ZeroDivisionError('Плохие новости')


for mode in [True, False]:
    try:
        do_zero_division(mode)
    except MyZeroDivision as mzd:
        print(mzd)
    except ZeroDivisionError as zd:
        pass
        print(zd)
