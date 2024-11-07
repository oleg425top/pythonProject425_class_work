'''Замыкание '''
def password_protect(password):

    def inner():
        if password == 'secret':
            return f'доступ разрешен'
            # print('Wellcome')
        else:
            return f'доступ запрещен'
            # print('Wrong password')
    return inner()
login = password_protect('secret')
print(login)
print(login)
login_1 = password_protect('no_secret')
print(login_1)
print(login_1)
print(password_protect('dfsdfds'))