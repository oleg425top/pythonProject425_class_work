# import os
#
# path_larning = r'C:\Users\oleg8\PycharmProjects\pythonProject425_class_work\module_04_funcs'
#
# for path, dirnames, filenames in os.walk(path_larning):
#     print(f'path  {path}')
#     print(f'dirnames  {dirnames}')
#     print(f'filenmaes  {filenames}')

import os


# path_larning = os.path.normpath(r'C:/Users\oleg8/PycharmProjects/pythonProject425_class_work/module_04_funcs')
# print(path_larning)
#
# for path, dirnames, filenames in os.walk(path_larning):
#     print(f'path  {path}')
#     print(f'dirnames  {dirnames}')
#     print(f'filenmaes  {filenames}')

# disk = 'C:\\'
# dir_1 ='Users'
# dir_2 ='PycharmProjects'
# dir_3 ='pythonProject425_class_work'
# dir_4 = 'module_06_files_01'
#
# path_module_06 = os.path.join(disk, dir_1, dir_2, dir_3, dir_4)
# print(path_module_06)
#
# for path, dirnames, filenames in os.walk(path_module_06):
#     print(f'path  {path}')
#     print(f'dirnames  {dirnames}')
#     print(f'filenmaes  {filenames}')

base_dir = '.'
dir = 'test_path_1'

path_base_test_dir = os.path.join(base_dir, dir)

for path, dirnames, filenames in os.walk(path_base_test_dir):
    print(f'path  {path}')
    print(f'dirnames  {dirnames}')
    print(f'filenmaes  {filenames}')
#
#
#
#
