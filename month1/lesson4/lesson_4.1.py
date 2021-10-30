#слова и множества
# lst = [1, 2, 3, 1, 4]
# set_1 = set()
# set_2 = set(lst)
# #добавление
# set_2.add(1)
# print(set_2)
# set_2 = {
#     1: "123",
#     2: "456"
# }
# print(set(lst))
# print(type(set_2))
# print(len(set_2))
#


menu = {
    "plov": {"рис", "мясо", "морковь"},
    "beshbarmak": {"мясо", "лапша", "лук"},
    "kasha": {"крупа", "молоко", "масло"}
}
guest = input("Choose: ")

for designation, ingridients in menu.items():
    if guest == designation:
        print(designation, ingridients)
    elif guest in ingridients:
        print(designation)
    else:
        print("goodbye")



# plov = {"рис", "мясо", "морковь"}
# beshbarmak = {"мясо", "лапша", "лук"}
#
# print(plov & beshbarmak)            #это пересечение,например:плов и бешбармак персекаются в мясе,поэтому на экран
# print(plov.intersection(beshbarmak)) #выводится "мясо"
#
# print(plov | beshbarmak)           #это объединение всех элементов или наборов,например:это как взять порцию плова
# print(plov.union(beshbarmak))     #и бешбармака и в одну кастрюлю все бросить
#
# print(plov - beshbarmak)   #это определение разности множеств,в данном случае в плове есть рис и морковь,которые
# print(plov.difference(beshbarmak)) #не содержатся в бешбармаке,поэтому на экран выводится "рис","морковь"
#
# print(plov ^ beshbarmak) #это работает уже наоборот , выводит на экран все,кроме одного совпадающего элемента
# print(plov.symmetric_difference(beshbarmak)) #в данном случае это "мясо"



