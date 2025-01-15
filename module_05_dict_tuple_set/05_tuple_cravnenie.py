my_tuple = 'Cat', 'Dog', 'Tiger', 'Bear',
my_tuple_2 = ('Cat', 'Dog', 'Tiger', 'Bear')

print(my_tuple == my_tuple_2)

my_tuple = 'Cat', 'Dog', 'Tiger', 'Bear',
my_tuple_2 = ('Tiger', 'Bear', 'Cat', 'Dog')

print(my_tuple == my_tuple_2)

my_tuple = 'Cat', 'Dog', 'Tiger', 'Bear',
my_tuple_2 = ('Tiger', 'Bear', 'Cat', 'Dog', 'Parrot')
print(len(my_tuple), len(my_tuple_2))
print(my_tuple < my_tuple_2)