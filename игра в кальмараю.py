import random
player1 = 10
comp = 10
rnd = 0
while True:
    rnd += 1
    print("hfasdkflhj;s")
    print("Кон", rnd)
    if rnd % 2 == 0:
        print("Загадывает comp, ты угадываешь")
        guessNum = random.randint(1, 5)

        guess = input("Четное или нечетное?(ч - четное, нч - нечетное)")

        if (guessNum % 2 == 0 and guess == 'ч') or (guessNum % 2 == 1 and guess == 'нч'):
            print("угадал, число равно ", guessNum)

            player1 += guessNum
            comp -= guessNum

        elif (guessNum % 2 == 1 and guess == 'ч') or (guessNum % 2 == 0 and guess == 'нч'):
            print("не угадал, число равно", guessNum)
            player1 -= guessNum
            comp += guessNum
        else:
            print("неправильно вводишь")
            continue
    elif rnd % 2 == 1:
        print("Загадываешь ты, comp угадывает")
        guessNum = int(input("Загадай число от 1 до 5"))
        guess = random.randint(1, 2)
        if(guess == 1 and guessNum % 2 == 1) or (guess == 2 and guessNum % 2 == 0):
            print("Comp угадал ваше число")
            comp += guessNum
            player1 -= guessNum
        elif (guess == 2 and guessNum % 2 == 1) or (guess == 1 and guessNum % 2 == 0):
            print("Comp не угадал ваше число")
            comp -= guessNum
            player1 += guessNum
    print(f"У вас {player1} шариков")
    print(f"У компьютера {comp} шариков")
    if comp <= 0:
        print("Congratuations!!!!")
        print("YOU WON")
        break
    if player1 <= 0:
        print("Game over")
        print("Comp выиграл")
        break