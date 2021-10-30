#дебильный калькулятор 1


what = input("Что делаем? ( +,-,*,**,/)")

a = float(input("введи первое число: "))
b = float(input("введи второе число: "))

if what == "+":
    c = a + b
    print("результат:" + str(c))

elif what == "-":
    c = a - b
    print("результат:" + str(c))
elif what == "*":
    c = a * b
    print("результат:" + str(c))
elif what == "**":
    c = a ** b
    print("результат:" + str(c))
elif what == "/":
    c = a / b
    print("результат:" + str(c))
else:
    print("ввели что-то не так")