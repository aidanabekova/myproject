# регулярные выражения
# import re
#
# my_text = "Vasya, 1998, vasya@gmail.com," \
#           "Adilet, 1907, adilet@intel.com," \
#           "Aidana, 2000, aidana@gmail.com," \
#           "Akylbek, 2003, akylbek@gmail.com," \
#           "Aman, 1999, aman@gmail.com," \
#           "Regina, 1999, regina@gmail.com"\
#           "Adilet, 1997, adiletspbek@yandex.ru"
#
# """
# \d = он ищет любые подряд стоящие числа [0-9]
# \D = он ищет любые не числа
# \w = люботный алфавитный символ[A-Z, a-z]
# \W = любой неалфавитный символ
# \s = ищет breakspace
# \S = ищет не breakspace
# [0-9]{любой порядок,который вам нужен} = аналог \d
# [A-Z a-z] + = ищем алфавитный порядок, + - это любая последовательность
# """

# searching = r"Adilet"
# searching = r"Vasya"
# results = re.match(searching, my_text)
# print(results)
# results = re.search(searching, my_text)
# print(results)
# results = re.findall(searching, my_text)
# print(results)

# searching = r"@\w+.\w+"
# results = re.findall(searching, my_text)
# print(results)
# searching = r"@(?!gmail\.com)(?!yandex\.ru)\w+.\w+"
# results = re.findall(searching, my_text)
# print(results)

import re

file_path = "/Users/aidana/PycharmProjects/pythonProject/month2/regularka/data.txt"
result_file_path = "/Users/aidana/PycharmProjects/pythonProject/month2/regularka/results.txt"
file_reader = open(file_path, mode="r", encoding='Latin-1')
results_file = open(result_file_path, mode="w", encoding="Latin-1")
my_text_1 = file_reader.read()

searching = r"[\w+_-]+@[\w+_-]+.[\w.]+"
results_all = re.findall(searching, my_text_1)

for item in results_all:
    print(item)
    results_file.write(item + "\n")

print(f"Total: {str(len(results_all))}")



