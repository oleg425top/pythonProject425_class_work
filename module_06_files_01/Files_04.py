import  os

base_dir = '.'
test_dir = 'test_path_1'

path_base_test_dir = os.path.join(base_dir, test_dir)

for path, dirnames, filenames in os.walk(path_base_test_dir):
    print(f'path  {path}')
    print(f'dirnames  {dirnames}')
    print(f'filenmaes  {filenames}')

new_dir = r'my_new_dir'

path_new_dir = os.path.join(base_dir, test_dir, new_dir)
print(path_new_dir)
# os.mkdir(path_new_dir)
# os.rmdir(path_new_dir)

print(os.path.abspath('.')) #путь к тому месты где мы находимся



