#ФУНКЦИИ И ИХ АРГУМЕНТЫ
# def menu(breakfast, lunch, dinner):
#     return {"завтрак": breakfast, "обед": lunch, "ужин": dinner}
#
# monday = menu("каша", "суп", "плов") #это правильно
# tuesday = menu("манты", "яичница", "пельмени") #это неправильно
# print(monday)
# print(tuesday)

def menu(drink, lunch, dessert="медовый торт"):
    return {"напиток": drink, "обед": lunch, "дессерт": dessert}

def show(dict1: dict):
    for i, k in dict1.items():
        print(i, "-", k)

monday = menu("компот", "суп", "брауни")
tuesday = menu(dessert="пирожное", drink="сок", lunch="омлет")
friday = menu("чай", "борщ")

show(monday)
show(menu(dessert="пирожное", drink="сок", lunch="омлет"))
# print(monday)
# print(tuesday)
# print(friday)

#создание функции и возращение чего-либо с помощью result
def plus(a, *args): #функция плюс принимала в себя только цифры,не именованые аргументы
    return a + sum(args)

print(plus(5,5,5,5))

def dct(**kwargs):   #фнкция кваргс принимает в себя именованые аргументы
    print(kwargs)
dct(a=1, b=2, c=3)













