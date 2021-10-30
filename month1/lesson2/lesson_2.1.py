# Условные конструкции и операторы сравнения,булеаны,циклы
# !=, <, >, =<, =>, not, or, and
#
name = "jack"
men = True
women = False

if men and women:
    print(True)


# while True:
#     nominal = input("Enter number")
#     if nominal == "1":
#         print("Абдулас Молдыбаев")
#     elif nominal == "5":
#         print("Бубусара Бейшеналиевна")
#     elif nominal == "10":
#         print("Касым Тыныстанов")
#         continue
#     elif nominal == "0":
#         print("Выход из цикла")
#         break
#     else:
#         print("Ввели что-то не так")

#
day = int(input("day: "))
month = int(input("month: "))
#
if day >= 21 and month == 3 or day <= 20 and month == 4:
    print("овен")
if day >= 21 and month == 4 or day <= 21 and month == 5:
    print("телец")
if day >= 22 and month == 5 or day <= 21 and month == 6:
    print("близнецы")
if day >= 22 and month == 6 or day <= 22 and month == 7:
    print("рак")
if day >= 23 and month == 7 or day <= 21 and month == 8:
    print("лев")
if day >= 22 and month == 8 or day <= 23 and month == 9:
    print("дева")
if day >= 24 and month == 9 or day <= 23 and month == 10:
    print("весы")
if day >= 24 and month == 10 or day <= 23 and month == 11:
    print("скорпион")
if day >= 24 and month == 11 or day <= 22 and month == 12:
    print("стрелец")
if day >= 23 and month == 12 or day <= 20 and month == 1:
    print("козерог")
if day >= 21 and month == 1 or day <= 19 and month == 2:
    print("водолей")
if day >= 20 and month == 2 or day <= 20 and month == 3:
    print("рыбы")

#
# for i in range(1, 11): #четные числа от 1 до 10
#     if i % 2 == 0:
#         print(i)
#
# for i in range(1, 10): #нечетные числа от 1 до 10
#     if i % 2 != 0:
#         print(i)





