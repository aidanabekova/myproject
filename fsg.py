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
#
# GeekTech = {
#     'address': 'Toktogula 175',
#     'courses': ['Android', 'Backend', 'Frontend'],
#     'bag': {'fails', 'errors', 'stack'}
# }
# # Удалить bag
# del GeekTech['bag']
#
# # Изменить адрес на нынешний
# GeekTech['address'] = 'Ibraimova 103'
#
# # Добавить номер телефона и инстаграмм аккаунт Гиктека
# GeekTech['phone_number'] = '+996507052018'
# GeekTech['instagram'] = '@geektech__kg'

# # Добавить/расширить список актуальными курсами, которые вы знаете. Затем преобразовать этот список в кортеж
# GeekTech2 = {
#     'courses': ['Android', 'Backend', 'Frontend', 'iOS', 'UX/UI designer', 'English'],
#     'phone_number': '+996507052018',
#     'instagram': '@geektech__kg'
# }
# GeekTech.update(GeekTech2)
# #GeekTech['courses'] = 'Android', 'Backend', 'Frontend', 'iOS', 'UX/UI designer', 'English'
# #print(GeekTech)
# GeekTech["courses"] = tuple(GeekTech["courses"])
# # Вывести словарь на экран с помощью цикла for с получением всех пар “ключ: значение”
# for key, value in GeekTech.items():
#     print(f'{key}: {value}')
#
# contacts = [
#     {'name': 'Geektech', 'phone': '0507052018'},
#     {'name': 'Служба спасения', 'phone': '911'},
#     {'name': 'Пожарная служба', 'phone': '101'},
# ]
#
#
# def create(name, phone):
#     contains = False
#     for i in contacts:
#         if (i['name'] == name or i['phone'] == phone):
#             contains = True
#             break
#     if (contains):
#         print("Такой контакт уже есть")
#     else:
#         contacts.append({"name": name, 'phone': phone})
#
#
# def edit(name, phone):
#     inContact = False
#     for i in contacts:
#         if (i['name'] == name):
#             inContact = True
#
#             i['phone'] = phone
#             break
#     if (not inContact):
#         print("такого имени в контакте нет")
#
#
# def delete(name):
#     inContact = False
#     for i in contacts:
#         if (i['name'] == name):
#             inContact = True
#             contacts.remove(i)
#     if (not inContact):
#         print("Нельзя удалить то чего нет")
#
#
# def showContacts():
#     print()
#     print("Список контактов")
#     print()
#     for i in contacts:
#         print(*i.values())
#
#
# create("vu", "0888234234")
# create("Ma", "0888234234")
# create("tym", "088823423")
# delete("Айдана")
# delete("tym")
# create("Айдана", "29428349924")
# edit("Айданфвыа", "ыфвжалофыва")
# showContacts()


#
# contacts = [
#     {'name': 'Geektech', 'phone': '0507052018'},
#     {'name': 'Служба спасения', 'phone': '911'},
#     {'name': 'Пожарная служба', 'phone': '101'},
# ]
#
# def show_all_contact(lst):
#     for i in lst:
#         print(*i.values())
#
#
# def add_number(lst):
#     show_all_contact(contacts)
#     for i in lst:
#         name = input('Enter name: ')
#         phone = input('Enter phone: ')
#         n = dict(name=name.title(), phone=phone)
#         lst.append(n)
#         if i['phone'] == phone:
#             print("It's number repeat\n"
#                   "Please write wrong!")
#         elif i['name'] == name:
#             print("It's number repeat\n"
#                   "Please write wrong!")
#         else:
#             show_all_contact(contacts)
#             break
#
#
# def edit_name(lst):
#     show_all_contact(contacts)
#     name = input('Введите имя для изминения:')
#     for i in lst:
#         if i['name'] == name:
#             n = input('Введите имя:')
#             phone = input('Введите номер:')
#             i['name'] = name
#             if i['name'] == n:
#                 print("Номер повторяется!\n"
#                       "Пожалуйста напишите неправильно!")
#             if i['phone'] == phone:
#                 print("Номер повторяется!\n"
#                       "Пожалуйста напишите неправильно!")
#             else:
#                 i['name'] = n
#                 i['phone'] = phone
#                 show_all_contact(contacts)
#                 break
#
#
# def delete_contact(lst):
#     show_all_contact(contacts)
#     name = input('Введите имя для удаления: ')
#     for i in lst:
#         if i['name'] == name:
#             lst.remove(i)
#             break
#
# def searching_contact(lst):
#     show_all_contact(contacts)
#     name = input('Введите имя для поиска:')
#     for i in lst:
#         if i['name'] == name:
#             print(i['name'])
#             print(i['phone'])
#
#
# while True:
#     command = input("Enter what we'll do: add = 'a', search = 's' edit = 'e' or delete = 'd' or 'q' for quite")
#     if command == 'a':
#         add_number(contacts)
#     elif command == 'e':
#         edit_name(contacts)
#     elif command == 's':
#         searching_contact(contacts)
#     elif command == 'd':
#         delete_contact(contacts)
#     elif command == 'f':
#         print('Программа завершина!')
#         break


contacts = [
    {'name': 'Geektech', 'phone': '0507052018'},
    {'name': 'Служба спасения', 'phone': '911'},
    {'name': 'Пожарная служба', 'phone': '101'},
]


def find_contact(lst):
    for contact in contacts:
        if contact['name'] == lst or contact['phone'] == lst:
            return contact


def add_contact(lst):
    name = input("Create new contact\nвведите имя: ").title()
    phone = input("введите номер: ")
    if find_contact(name) or find_contact(phone):
        print('Такой контакт уже есть!')
        q = input('хотите добавить ворой номер?  д/н: ')
        if q == 'д':
            for i in lst:
                if i['name'] == name:
                    phone = input("введите второй номер: ")
                    i.update((dict(second_phone=phone)))
    else:
        contact = dict(name=name.title(), phone=phone)
        lst.append(contact)
        return contact


def edit_contact(lst):
    name = input("введите имя: ").title()
    for i in lst:
        if i["name"] == name:
            n = input("введите новое имя: ")
            phone = input("введите новый номер: ")
            if find_contact(n) or find_contact(phone):
                print('контакт уже существует!')
            else:
                i["name"] = n
                i["phone"] = phone
        else:
            print("контакт не существует")


def delete_contact(lst):
    name = input("введите имя: ").title()
    for i in lst:
        if i["name"] == name:
            lst.remove(i)


def show_all_contacts(lst):
    print("_____CONTACTS_____")
    for i in lst:
        print(*i.values())


def main():
    while 1:
        show_all_contacts(contacts)
        command = input("введите команду ' 1 - edit / 2 - delete / 3 - add'. ' 0 - q' for quite: ").lower()
        if command == 'edit' or command == '1':
            edit_contact(contacts)
        elif command == 'delete' or command == '2':
            delete_contact(contacts)
        elif command == 'add' or command == '3':
            add_contact(contacts)
        elif command == 'q' or command == '0':
            print("программа завершена")
            break
        else:
            print('неверная команда!')


main()
