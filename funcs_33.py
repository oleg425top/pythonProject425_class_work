'''каринг'''

# def greet(greeting , name):
#     print(f"{greeting}, {name}")
#
# greet('hello', 'Oleg')

def greet_curried(greeting):
    def greet (name):
        print(f"{greeting}, {name}")

    return greet
greet_hello = greet_curried('Hello')
# print(greet_hello('jkhkjh'))
greet_hello("Ivan")
greet_hello('Oleg')
