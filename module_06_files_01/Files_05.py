# """конструкция open/close"""
#
# file = open(r'test_path_1/test_1.txt', 'rt', encoding ='UTF-8' )
# content = file.read()
# file.close()
# print(content)
#
#
# '''конструкция with open'''
# with open(r'test_path_1/test_1.txt', 'rt', encoding ='UTF-8') as file:
#     content = file.read()
# print(content)

file = open(r'test_path_1/test_1.txt', 'rt', encoding ='UTF-8' )
for lines in file:
    print(lines, end='')
file.close()
print()
with open(r'test_path_1/test_1.txt', 'rt', encoding ='UTF-8') as file:
    for line in file:
        print(line, end='')