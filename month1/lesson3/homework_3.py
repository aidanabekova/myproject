data_tuple = ("h", 6.13, "C", "e", "T", True, "k", "e", 3, "e", 1, "g")

letters = []
numbers = []

for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)
print(letters)
print(numbers)

numbers.remove(numbers[0])
print(numbers)

# letters.append(numbers[0])
# print(letters)
#
# numbers.remove(numbers[0])
# print(numbers)

o = numbers.pop(0)
letters.append(o)
print(letters)


numbers.insert(1, 2)
print(numbers)

numbers.sort()
print(numbers)

letters.reverse()
print(letters)
letters[1] = "G"
letters[7] = "c"
print(letters)

letters = tuple(letters)
numbers = tuple(numbers)
print(letters)
print(numbers)







