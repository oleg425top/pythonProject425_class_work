def my_space_addres_mix(name:str, age=36, city=None,*args,**kwargs):
    print(name)
    print(age)
    if city:
        print(city)
    if args:
        for item in args:
            print(item)
    if kwargs:
        for key, value in kwargs.items():
            print(key, value)

my_space_addres_mix('Oleg', 36, 'Sterlitamak', 'Bachkortostan', 'Ural', planet='Earth', star='Sun')
print()
my_space_addres_mix('Oleg', planet='Earth', star='Sun')