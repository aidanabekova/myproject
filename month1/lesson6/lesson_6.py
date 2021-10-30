
from random import randint
print(randint(1, 23))


#лямда
# a = lambda a, b: a + b #это создание лямды,т.е у лямды сперва идет само слово лямда,потом идут ее параметры(a,b)
# print(a(2, 3))       #затем идет ее выражение(2,3)
# print(type(a))
#
# b = (lambda x, y=2: x + y)(4, 6)
# print(b)
#
# print(10 + (lambda x: x ** 2)(2)) #еще один пример лямды
#
# words = ["kg", "kz", "ru", "ua"]
# names = ["adil", "samat", "erkin", "max", "azamat", "abdraim"]
# # # def up_l(word):
# # #     return word.upper()
# # # def edit_f(lst, func):
# # #     for word in lst:
# # #         print(func(word))
# # #
# # # # edit(words, up_l)
# # # edit_f(names, up_l)
# #
# edit_l = list(map(lambda word: word.upper(), words))
# print(edit_l)
# print(list(map(lambda word: word.upper(), names)))
#
# #print(list(filter(lambda word: len(word) > 3, names)))
# filtered_names = list(filter(lambda word: not word.startswith("a"), names))
# print(filtered_names)




