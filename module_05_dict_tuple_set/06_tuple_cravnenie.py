animals_tuple_1 = ('Cat', 'Dog', 'Tiger', 'Bear')
animal = input('введи животное')
if animal in animals_tuple_1:
    print(f'({animal}) есть в списке')
else:
    print("такого нет")

for anim in animals_tuple_1:
    print(anim)

for i in range(len(animals_tuple_1)):
    print(animals_tuple_1[i])