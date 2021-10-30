#модули, рандом

import random
from random import choice
from datetime import datetime
import time

start = datetime.now()
print(start)
time.sleep(5)
end = datetime.now() - start
print(end)


def timer(num):
    while num !=0:
        num -= 1
        time.sleep(1)
        print(num)
timer(15)


#students = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23]
#
# while len(students) != 0:
#     q = input("продолжать y/n")
#     if q == "y".lower():
#         # # number = random.choice(students)
#         print(students.pop(students.index(random.choice(students))))
#         # students.remove(number)
#         print(students)
#     elif q == "n".lower():
#         print("программа завершена")
#         break



# from random import randint, choice, randrange, sample
# print(randint(5, 10))
# tpl = 1, 2, 3, 4, 5
# print(choice(tpl))
# print(sample(tpl, 2))
# print(randrange(1, 10, 5))



