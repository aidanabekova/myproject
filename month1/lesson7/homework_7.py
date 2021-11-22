#Написать программу, которая загадывает одно случайное число от 1 до 100, а пользователь старается угадать.
#  1)Программа должна запрашивать у пользователя целое число, в бесконечном цикле, пока оно не будет отгадано.
#  2)Исключать ошибки ввода букв и ограничить ввод числа больше 100 и меньше 0, подсказывать пользователю корректный
#  ввод для каждого отдельного случая.
#  3)Если пользователь отгадал число, вывести на экран количество потраченных попыток и секунд затем выйти из программы.
#  4)Программа должна подсказывать знаком “>” или “<” и “очень близко” при радиусе 5 и “близко” при 10.
import random
import time

rand = random.randint(1, 100)
attempts = 0
start_time = time.time()
while True:
    try:
        num = int(input("введите любое целое число: "))
        attempts += 1
        if num < 1 or num > 100:
            print("введите числобольше 0 и меньше 100!")
            continue
    except:
        print("буквы вводить нельзя!")
        continue

    if rand == num:
        print(f"потраченное время {round(time.time()-start_time)} секунд\nколичество попыток: {attempts}")
        break
    if num > rand:
        print("загаданное компьютером число меньше")
    if num < rand:
        print("загаданное компьютером число больше")

    if abs(num-rand) <= 5:
        print("очень близко")
    elif abs(num - rand) <= 10:
        print("близко")
    else:
        print("очень далеко")

import random
import time
start = time.time()
print(start)
random_number = random.randint(1, 100)
i = 0
while True:
    try:
        answer = int(input(f"Введите число!"))
        i += 1
        if answer < 1 or answer > 100:
            print("введите целое число меньше 101 и больше 0")
            continue
    except ValueError:
        print("вводить можно тольео буквы")
        continue
    if answer == random_number:
        print("вы угадали число поздравляем")
        print(f" количество попыток: {i}")
        print(f" прошло {time.time()-start} секунд")
        break
    if answer > random_number:
        print("загаданное число меньше")
    if answer < random_number:
        print("загаданное число больше")

    if abs(answer - random_number) <= 5:
        print("очень близко")
    elif abs(answer - random_number) <= 10:
        print("близко")
    else:
        print("вообще не близко")






