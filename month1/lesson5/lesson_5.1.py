# #оборачивание все в функцию
# def auto_code(code):
#     if code == "01" or code == "1":
#         print("Bishkek city")
#     elif code == "02" or code == "2":
#         print("Osh city")
#     elif code == "03" or code == "3":
#         print("Batken")
#     elif code == "04" or code == "4":
#         print("Dzhalal-Abad")
#     elif code == "05" or code == "5":
#         print("Naryn")
#     elif code == "06" or code == "6":
#         print("Osh")
#     elif code == "07" or code == "7":
#         print("Talas")
#     elif code == "08" or code == "8":
#         print("Chui")
#     elif code == "09" or code == "9":
#         print("Issyk-Kul")
#     else:
#         print("Ошибка,повторите попытку!")
#
# auto_code("08")
# auto_code("7")
members = [
    {"name": "Azat", "age": 18, "height": 185, "physic": True},
    {"name": "Adilet", "age": 17, "height": 180, "physic": False},
    {"name": "Asan", "age": 20, "height": 179, "physic": True},
]

soldiers = []

def selection_army(member_lst):
    for member in member_lst:
        if member["age"] >= 18 and member["height"] >= 180 and member["physic"] == True:
            member["soldier"] = True
            soldiers.append(member)
    print(soldiers)
selection_army(members)

def add_member(name, age, height, physic):
    return{"name": name, "age": age, "height": height, "physic": physic}

members.append(add_member("Ulan", 19, 181, True))
selection_army(members)

def find(name: str, lst: list):
    for member in lst:
        if member["name"] == name.title():
            return member
    print("Объект не найден")

print(find("zheka", members))





