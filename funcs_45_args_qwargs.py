def remove_from_str(string, *args):
    for symbol in args:
        string = string.replace(symbol, len(symbol)*'*')
    return string

print(remove_from_str('Смотри пидрила, я тебя в рот выебу!!', "пидрила","выебу"))