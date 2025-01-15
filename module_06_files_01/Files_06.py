# from idlelib.iomenu import encoding
#
# from module_04_funcs.funcs_30 import result

quests_count = 0
# with open('qwests.txt', 'r', encoding = 'utf-8') as file:
#
#     for line in file:
#         print(line.rstrip())
#         quests_count += 1
#     print(f'количество гостей равно: {quests_count}')

with open('qwests.txt', 'r', encoding = 'utf-8') as file:
    quests_list = file.readlines()
    print(quests_list)
print(''.join(quests_list))
print(f'количество гостей:  {len(quests_list)}')
