''' замыкание'''

def make_closer (par):
    loc = par
    def power (par):
        return par ** loc
    return power

f_square = make_closer(2)
f_cube = make_closer(3)
for i in range (5):
    print(f" {i} - квадрат {f_square(i)}; куб {f_cube(i)}")