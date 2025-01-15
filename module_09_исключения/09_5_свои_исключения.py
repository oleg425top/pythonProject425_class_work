class SushiError(Exception):
    def __init__(self, sushi, message):
        super().__init__(message)
        self.sushi = sushi


class TooFewRiceError(SushiError):
    def __init__(self, sushi, rice, message):
        super().__init__(sushi, message)
        self.rice = rice


class TooMuchRiceError(SushiError):
    def __init__(self, sushi, rice, message):
        super().__init__(sushi, message)
        self.rice = rice


def make_sushi(sushi, rice):
    if sushi not in ['california', 'philadelpia', 'yamato']:
        raise SushiError(sushi, 'Позиции нет в меню')
    if rice < 50:
        raise TooFewRiceError(sushi, rice, 'Слишком мало риса')
    elif rice > 100:
        raise TooMuchRiceError(sushi, rice, 'Cлишком много риса')

    return 'ваши суши готовы'


for (sushi, rice) in [('philadelpia', 55), ('bismark', 70), ('california', 5), ('yamato', 150)]:
    try:
        print(make_sushi(sushi, rice))
    except TooFewRiceError as TFRE:
        print(f'{TFRE}: {TFRE.sushi}, {TFRE.rice}')
    except TooMuchRiceError as TMRE:
        print(f'{TMRE}: {TMRE.sushi}, {TMRE.rice}')
    except SushiError as SE:
        print(f'{SE}: {SE.sushi}')
