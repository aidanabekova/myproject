from random import randint
from datetime import datetime

player = randint(1, 6), randint(1, 6)
comp = randint(1, 6), randint(1, 6)

attempts = int(input("введите количество попыток: "))

cash = 100

while attempts != 0:
    player = [randint(1, 6), randint(1, 6)]
    comp = [randint(1, 6), randint(1, 6)]
    if cash == 0:
        print("you lost")
        break
    attempts -= 1
    print(cash)
    bet = int(input(f"Сделай ставку: Доступно: {cash}"))
    if bet < 1 or bet > cash:
        print("ставка не должна превышать сумму")
        continue
    attempts -= 1
    print(attempts)
    if attempts == 0:
        player = [randint(1, 2), randint(1, 3)]
        comp = [randint(4, 6), randint(1, 6)]
    if sum(player) > sum(comp):
        cash += bet
    elif sum(player) < sum(comp):
        cash -= bet
    else:
        pass
    with open("res.txt", "w") as result:
        result.write(f"player: {player}, comp: {comp}, {cash} \n")

    print(cash)

    print("player: ", player)
    print("comp: "), comp
