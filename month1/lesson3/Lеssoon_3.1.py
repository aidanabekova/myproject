vowels = ("a", "e" "i", "y", "o", "u")
consonats = ("q", "w", "r", "t", "p", "s", "d", "f", "g",  "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m")

# vowels - гласные
# consonats - согласные

vowels_list = []
consonats_list = []

print(len(vowels))

count = 0
while True:
    count += 1
    word = input("введи слово: ").lower()

    for letter in word:
        if letter in vowels:
            vowels_list.append(letter)
        elif letter in consonats:
            consonats_list.append(letter)

print(vowels_list)
print(consonats_list)


# tpl = tuple()
# tpl1 = ()
#
# numbers = (1, 2, 3, 4)
# text = ("abc", "efg")
# # print(id(numbers))
#
# numbers = numbers + text
# print(numbers)
# # print(id(numbers))
#
# numbers = list(numbers) #преобразование кортежа в список
# print(type(numbers))
# numbers.append(5)
# numbers.remove(3)
# numbers[1] = 20
# numbers.insert(4, "EXO")
# print(numbers)
