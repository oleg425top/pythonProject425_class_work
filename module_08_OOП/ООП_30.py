import copy


class SampleClass:
    def __init__(self, val):
        self.val = val

obj_1 = SampleClass(0)
obj_2 = SampleClass(2)
obj_3 = obj_1
# obj_3 = copy.deepcopy(obj_1) пример копирроания

print(obj_1 is obj_2)
print(obj_2 is obj_3)
print(obj_1 is obj_3)
print(obj_3 is obj_1)

str_1 = 'У мэри был'
str_2 = 'У мэри был барашек'
str_1 += 'барашек'
str_3 = str_1
print(str_1 == str_2, str_1 is str_2, str_1 == str_3, str_1 is str_3)