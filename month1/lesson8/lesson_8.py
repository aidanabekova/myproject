#работа с файлами
import time

with open("result.txt") as gmn:
    for line in gmn:
        for i in line:
            print(i, end="")
            time.sleep(0.1)

# from pprint import pprint
#
# with open("file.txt", "w") as file:
#     file.write("my name is aidana \n")
#
# with open("file.txt", "a") as file:
#     file.write("i'm from USA \n")
#
#
# with open("file.txt", "r") as file:
#     pprint(file.read())