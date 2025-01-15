import os

path_larning = r'C:\Users\oleg8\PycharmProjects\pythonProject425_class_work\module_06_files_01'
print(os.path.isabs(path_larning))
print(os.path.isfile(path_larning))
print(os.path.isdir(path_larning))
print(os.path.islink(path_larning))