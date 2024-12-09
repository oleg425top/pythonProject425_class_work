try:
    i = int('Hello')
except Exception as e:
    print(f'тип ошибки ({e})')
    print(e.__str__())
finally:
    print(f'Ok')