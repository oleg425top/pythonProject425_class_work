'''каринг'''

def greet_deeply_curid(greeting):
    def w_separator(separate):
        def w_emphasis(emphasis):
            def w_name(name):
                print(greeting + separate + emphasis + name)

            return w_name

        return w_emphasis

    return w_separator
greet = greet_deeply_curid('Hello')('/.../')
print(greet_deeply_curid('Gooddbye')(', ')('Vasiliy')('!!!!'))
greet('Dima')('111')
greet('Oleg')('779789')
greet_deeply_curid('Hello')('/.../')('!')