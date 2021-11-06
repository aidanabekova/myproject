user = int(input("ваше загаданное число:"))
min_number = 1
max_number = 100
attempts = 0
while True:
    mid = (min_number + max_number) // 2
    print("comp: ", mid)
    answer = input("да/больше/меньше")
    attempts += 1

    if answer == 'да':
        print("Количество попыток", attempts)
        if user == mid:
            print("комп угадал ваше число")
        if user != mid:
            print("комп не угадал ваше число")
            print("ты неправильно подсказывал")
        break
    elif answer == "больше":
        min_number = mid
    elif answer == "меньше":
        max_number = mid
    else:
        print("вводите правильно!")
        attempts -= 1
