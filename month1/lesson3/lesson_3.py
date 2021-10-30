# list1 = list()
# list2 = []
#
#
# for number in range(1, 6):
#     list2.append(number)
list3 = [5, 2.5, 1, 8, 3, 6, 4]

odds = [] #нечетные числа
evens = [] #четные числа

for i in list3:
    if i % 2 == 0:
        evens.append(i)
    elif i % 2 != 0:
        odds.append(i)

print(sorted(odds))
print(sorted(evens))


# print(sorted(list3, reverse=True))
# print(list3)

# list3.sort()
# print(list3)
#
# list3.reverse()
# print(list3)
# print(list3)
# print(list3[5][1])

# print(list3[-1]) #Индексация
# print(list3[1:4]) #Отрезок,т.е от какого до какого числа нужно вывести на экран
# print(list3[1:4:2]) #Здесь уже добавлен шаг с которым выводятся числа,т.е через одну числа выводятся на экран
# print(list3[-1::-1])

# #Добавление в список
# list1.append("Azamat")
# print(list3 + list1)
#
# list3.extend(list2)
# print(list3)
#
# list3.insert(2, "word")
# list3.insert(3, "it")
# print(list3)

# print(list1)
#
# #Удаление из списка
# list3.remove(list3[0])
# print(list3)
#
# del list3[-2]
# print(list3)
# # del list3[3:]
# del list3[3], list3[2]
# print(list3)

# #Изменение чего-либо в списке
# list1[0] = "Adilet"
#list3[1] = 50
# print(list1)