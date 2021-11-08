# user = int(input("ваше загаданное число:"))
# min_number = 1
# max_number = 100
# attempts = 0
# while True:
#     mid = (min_number + max_number) // 2
#     print("comp: ", mid)
#     answer = input("да/больше/меньше")
#     attempts += 1
#
#     if answer == 'да':
#         print("Количество попыток", attempts)
#         if user == mid:
#             print("комп угадал ваше число")
#         if user != mid:
#             print("комп не угадал ваше число")
#             print("ты неправильно подсказывал")
#         break
#     elif answer == "больше":
#         min_number = mid
#     elif answer == "меньше":
#         max_number = mid
#     else:
#         print("вводите правильно!")
#         attempts -= 1

GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
# Удалить bag
del GeekTech['bag']

# Изменить адрес на нынешний
GeekTech['address'] = 'Ibraimova 103'

# Добавить номер телефона и инстаграмм аккаунт Гиктека
GeekTech['phone_number'] = '+996507052018'
GeekTech['instagram'] = '@geektech__kg'

# Добавить/расширить список актуальными курсами, которые вы знаете. Затем преобразовать этот список в кортеж
GeekTech2 = {
    'courses': ['Android', 'Backend', 'Frontend', 'iOS', 'UX/UI designer', 'English'],
    'phone_number': '+996507052018',
    'instagram': '@geektech__kg'
}
GeekTech.update(GeekTech2)
#GeekTech['courses'] = 'Android', 'Backend', 'Frontend', 'iOS', 'UX/UI designer', 'English'
#print(GeekTech)
GeekTech["courses"] = tuple(GeekTech["courses"])
# Вывести словарь на экран с помощью цикла for с получением всех пар “ключ: значение”
for key, value in GeekTech.items():
    print(f'{key}: {value}')

