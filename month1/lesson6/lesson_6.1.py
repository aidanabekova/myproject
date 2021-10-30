#исключения

names = ["adil", "samat", "erkin", "max", "azamat", "abdraim"]

filtered_names = list(filter(lambda word: word.startswith("a"), names))

#print(filtered_names)
def index_list(lst):
    while True:
        try:
            position = int(input("введите индекс"))
            # position = int(position)
            print(lst[position])
        except IndexError:
            print(f"Вводите от 0 до {len(names)-1}")
        except:
            print("вы ввели совсем не то!")
index_list(filtered_names)

