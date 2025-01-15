import pickle

my_dict = {
    'nums': [1, 2, 3, 4],
    'strings': ['charger_string', b'byte_string'],
    'other': [None, True, False]
}
# для обычной работы
# пиклинг
my_data = pickle.dumps(my_dict, pickle.HIGHEST_PROTOCOL)
print(my_data)
# анпиклинг
my_data_ds = pickle.loads(my_data)
print(my_data_ds)

with open('data_picle.pdf', 'wb') as fp:
    pickle.dump(my_data_ds, fp, protocol=5)

try:
    with open('data_picles.pkl', 'rb') as fp:
        my_data_ff = pickle.load(fp)
except FileNotFoundError:
    print('File not Find!!!')
print(my_data_ff)
