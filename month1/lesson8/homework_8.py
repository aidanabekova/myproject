         #Создать программу “Таблица умножения”.
# 1)Программа должна запрашивать у пользователя имя и количество попыток. Затем работать в бесконечном цикле
         # до истечения указанных попыток.
# 2)Программа должна запрашивать произведение двух случайных чисел от 1 до 9. \
# После ввода пользователем ответа, выводить на экран правильный ответ.
# 3)Каждый вопрос-ответ записывать в файл results.txt
# # 4)В этот же файл дописать итоговый отчёт с указанием имени, количества попыток и затраченного времени

from random import randint
import datetime


name = input("Ваше имя: ")
attempts = int(input("Введите количество попыток: "))
copyattempts = attempts
start = datetime.datetime.now()

while True:
    num1 = randint(1, 9)
    num2 = randint(1, 9)
    action = num1 * num2
    print(f"Сколько будет {num1} x {num2} = ?", end=' ')
    result = int(input())
    print(action)
    attempts -= 1

    with open('results.txt', 'a') as file:
        if result == action:
            file.write(f"{num1} x {num2} = {result} ({action}) правильно\n")
        elif result != action:
            file.write(f"{num1} x {num2} = {result} ({action}) неправильно\n")

    if attempts == 0:
        end = datetime.datetime.now()
        end - start
        with open('results.txt', 'a') as file:
            file.write(
                f"истраченные попытки: {copyattempts},"
                f"истраченное время: {(datetime.datetime.now() - start).seconds} секунд, "
                f"имя: {name}\n"
            )
        print("Все попытки были истрачены")
        print(f"Затраченное время: {end - start} секунд")
        break


