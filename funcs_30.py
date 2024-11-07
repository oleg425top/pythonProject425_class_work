'''Замыкание '''
def outer(par):
    loc = par

    def inner():
        return loc

    return inner


var =1
outer(var)
result = outer(var)
print(result())