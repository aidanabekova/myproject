#словари и множества                     #ПРОЧИТАТЬ ПРО ВСЕ МЕТОДЫ СЛОВАРЕЙ

names = ("one", "two", 'three', "four")
numbers = 1, 2, 3, 4

for i in range(1, 5):
    numbers.append(i)
dict_3 = dict(zip(numbers, names))

if 3 in dict_3:
    print(dict_3[3])

print(names)
print(numbers)
print(dict_3)

print(len(names))
print(len(numbers))
dict_4 = dict([(2, 'fgh'), (9, 'mhb'), (names, 'three'), (numbers, 'cvbn')])
print(dict_4)
# создание словаря
dict_1 = {
    "def": 1,
    "if": 2,
    "three": 3,
    "four": 4,
    "numbers": [1, 2, 3],
    "names": names
}
print(dict_1[names])

# удаление из словаря
del dict_1["names"]
dict_1.pop("numbers")
print(dict_1)

student = dict(name="Azat", age="19")
print(student)
# добавление в словарь и изменение словаря
dict_1["five"] = 5
dict_1["def"] = "definition"
dict_1["if"] = "condition"
print(dict_1)

print(student)
print(dict_1)
# совмещение двух словарей
dict_1.update(student)
print(dict_1)
a = {**dict_3, **dict_4}
print(a)

for key in dict_1.keys():
    print(key)

for value in dict_1.values():
    print(value)

for key, value, in dict_1.items():
    print(key, "- это", value)







