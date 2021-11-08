# задание No1
# 1. Создать 4 класса и с помощью их преобразить РОМБОВИДНЫЙ тип множественного наследования
# 2. У супер класса должны быть не меньше 4 атрибутов
# 3. У каждого класса должно быть не меньше 2 методов
# 4. Также должны быть соблюдены def __str__(self) + super()
# 5. И к каждому классу создать объект ( в итоге будет не меньше 4 объектов

class C:
    def __init__(self, name, OOP, year_of_issue, developer):
        self.name = name
        self.OOP = OOP
        self.year_of_issue = year_of_issue
        self.developer = developer

    def application(self):
        return f"The {self.name} was originally created for systems programming, so it isn't surprising " \
               f"that it's so actively used in the creation of operating systems and software"

    def peculiarity(self):
        return f"{self.name} is one of the earliest programming languages"

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"OOP: {self.OOP}\n" \
               f"Year of issue: {self.year_of_issue}\n" \
               f"Developer: {self.developer}\n"


language1 = C(name="Language C",
              OOP=True, year_of_issue="1969 - 1973",
              developer="Dennis Ritchie")


# print(language1)
# print(language1.application())
# print()
# print(language1.peculiarity())
# print("~" * 163)


class C_pp(C):

    def application(self):
        return f"{self.name} is used in all areas of programming:" \
               f"from high-load systems to microcontroller programming"

    def peculiarity(self):
        return f"{self.name} is one of the earliest programming languages"

    def __str__(self):
        return super(C_pp, self).__str__()


language2 = C_pp(name="Language C_pp", OOP=True,
                 year_of_issue=1985, developer="Bjorn Stroustrup")


# print(language2)
# print(language2.application())
# print()
# print(language2.peculiarity())
# print("~" * 103)


class C_sharp(C):

    def application(self):
        return f"{self.name} can be used to create web-applications"

    def peculiarity(self):
        return f"{self.name} is one of the earliest programming languages"

    def __str__(self):
        return super(C_sharp, self).__str__()


language3 = C_sharp(name="language C_sharp", OOP=True,
                    year_of_issue=2002, developer="Anders Hejlsberg")


# print(language3)
# print(language3.application())
# print()
# print(language3.peculiarity())
# print("~" * 55)

class BAB(C_sharp, C_pp):

    def application(self):
        return f"{self.name} is a very universal programming language in which you can create" \
               f"applications, websites, it's even suitable for artificial intelligence"

    def peculiarity(self):
        return f"{self.name} was created jointly with the alumni of GeekTech py.13"

    def __str__(self):
        return super(BAB, self).__str__()


language4 = BAB(name="Language BAB", OOP=True,
                year_of_issue=2041, developer="Bekova Aidana")


# print(language4)
# print(language4.application())
# print()
# print(language4.peculiarity())
# print("~" * 148)


# Задание No 2
# 1. Создать 4 класса , один из них является супер-классом , от которого наследуются все остальные 3 класса
# 2. У супер класса должно быть как минимум 4 атрибута ( def __init__(self, atribut, atribut2): )
# 3. У каждого класса должно быть как минимум 2 метода ( def method(self): )
# 4. Также должны быть соблюдены def __str__(self) + super()
# 5. К каждому классу создать по одному объекту ( в итоге должно быть 4 объекта)

class Coca_Cola:
    def __init__(self, name, color, country, cost_drink):
        self.name = name
        self.color = color
        self.country = country
        self.cost_drink = cost_drink

    def history(self):
        return f"{self.name} was invented in Atlanta (Georgia, USA) on May 8, 1886 by pharmacist John Stith Pemberton"

    def interesting_fact(self):
        return f"В составе первой версии {self.name} был КОКС"

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Color: {self.color}\n" \
               f"Country: {self.country}\n" \
               f"Cost of the drink: {self.cost_drink}\n"


drink1 = Coca_Cola(name="Coca-Cola", color="black", country="USA", cost_drink="85 som")


# print(drink1)
# print(drink1.history())
# print()
# print(drink1.interesting_fact())
# print("=" * 148)

class Sprite(Coca_Cola):
    def __init__(self, name, color, country, cost_drink, new_taste):
        super(Sprite, self).__init__(name, color, country, cost_drink)
        self.new_taste = new_taste

    def history(self):
        return f"Company Coca-Cola first released {self.name} in October 1961 in Germany."

    def interesting_fact(self):
        return f"В спрайте никогда не было кокса:), а если серьезно,то в начале 2000-х годов {self.name} вошёл \n" \
               f"в пятёрку самых" \
               f" употребляемых безалкогольных газированных напитков планеты."

    def __str__(self):
        return super(Sprite, self).__str__() + f"New taste: {self.new_taste}\n"


drink2 = Sprite(name="Sprite", color="colorless", country="USA", cost_drink="75 som", new_taste="cucumber taste")


# print(drink2)
# print(drink2.history())
# print()
# print(drink2.interesting_fact())
# print("=" * 148)

class Fanta(Coca_Cola):
    def __init__(self, name, color, country, cost_drink, bottle_shape):
        super(Fanta, self).__init__(name, color, country, cost_drink)
        self.bottle_shape = bottle_shape

    def history(self):
        return f"{self.name} appeared in 1940 in Germany during the Second World War"

    def interesting_fact(self):
        return f"Производство {self.name} началось от безысходности. \n" \
               f"Антигитлеровская коалиция наложила эмбарго на поставки продуктов в Германию. \n" \
               f"Из-за этого прекратилось поступление сиропа из США, являющегося основным ингредиентом Кока-колы. \n" \
               f"Заводу грозило банкротство. \n" \
               f"Макс Кайт предложил рецепт напитка на основе яблочного жмыха и молочной сыворотки"

    def __str__(self):
        return super(Fanta, self).__str__() + f"Bottle shape: {self.bottle_shape}\n"


drink3 = Fanta(name="Fanta", color="orange", country="USA", cost_drink="80 som", bottle_shape="90-60-90")


# print(drink3)
# print(drink3.history())
# print()
# print(drink3.interesting_fact())
# print("=" * 148)


class Dobryi(Coca_Cola):
    def __init__(self, name, color, country, cost_drink, number_of_species):
        super(Dobryi, self).__init__(name, color, country, cost_drink)
        self.number_of_species = number_of_species

    def history(self):
        return f"in 2005 {self.name} became part of the Coca-Cola system in Russia."

    def interesting_fact(self):
        return f"Сок {self.name} был создан в Росии, но потом Coca-Cola выкупила этот напиток"

    def __str__(self):
        return super(Dobryi, self).__str__() + f"Number of species: {self.number_of_species}\n"


drink4 = Dobryi(name="Dobryi", color="green", country="Russia", cost_drink="120 som", number_of_species=12)

# print(drink4)
# print(drink4.history())
# print()
# print(drink4.interesting_fact())
# print("=" * 148)


# Задание No3
# 1. Создать 2 класса с магическими методами
# 2. 1-ый класс это класс Кинотеатр , в котором будут фильмы и нужно
# использовать как минимум 2 магических метода для выведения фильма
# 3. Должен быть выбор фильмов и цена у каждого разный
# 4. 2-ой класс это класс Старбакс в котором пишут имена на кофе
# 5. Если имя больше 9 символов пишут только 5 символов имени
# 6. Если имя меньше 5 пишут все символы имени
# 7. Использовать именно магические методы

import random


class Cinema:
    def __init__(self, name, country, film_director, genre, year_of_issue, ticket):
        self.name = name
        self.country = country
        self.film_director = film_director
        self.genre = genre
        self.year_of_issue = year_of_issue
        self.ticket = ticket

    def __add__(self, other):
        if (isinstance(other, list)):
            other.append(self)
            return other
        else:
            return [self, other]

    def info(self):
        hall = random.randint(1, 5)
        minutes = random.randint(1, 6) * 10
        return f"Ticket price {self.ticket}$, the session will start in {minutes} minutes in hall {hall} "

    def __str__(self):
        return f"Movie title: {self.name}\n" \
               f"Country: {self.country}\n" \
               f"Film director: {self.film_director}\n" \
               f"Film genre: {self.genre}\n" \
               f"Year of issue: {self.year_of_issue}\n" \
               f"Ticket price: {self.ticket}\n"


def choice(moviename):
    for i in movieListView:
        if i.name == moviename:
            print(i.info())


shang_chi = Cinema(name="Shang-Chi", country="USA", film_director="Destin Daniel Cretton",
                   genre="action, adventure, fantasy", year_of_issue=2021, ticket=15)
kingdom = Cinema(name="Kingdom", country="Japan", film_director="Shinsuke Sato",
                 genre="action, military, history", year_of_issue=2019, ticket=13)
twilight = Cinema(name="Twilight", country="USA", film_director="Catherine Hardwicke",
                  genre="melodrama, fantasy, comedy", year_of_issue=2008, ticket=18)
parasites = Cinema(name="Parasites", country="South Korea", film_director="Bong Joon Ho",
                   genre="comedy drama, thriller", year_of_issue=2019, ticket=20)
wind = Cinema(name="Wind", country="South Korea", film_director="Bong Joon Ho",
              genre="comedy drama", year_of_issue=2010, ticket=30)

movieListView = shang_chi + kingdom
movieListView = twilight + movieListView
movieListView = parasites + movieListView
movieListView = wind + movieListView


# showMovie = ""
# for movie in movieListView:
#     print(movie)
#     showMovie += movie.name + ", "
#
# while 1:
#
#     f = input(f"Select a movie({showMovie}): ")
#     choice(f)
#     if (f == 'quit'):
#         print("quit")
#         break
# 4. 2-ой класс это класс Старбакс в котором пишут имена на кофе
# 5. Если имя больше 9 символов пишут только 5 символов имени
# 6. Если имя меньше 5 пишут все символы имени
# 7. Использовать именно магические методы

class Starbucks:
    def __init__(self, starbucks_branch, place, *names):
        self.starbucks_branch = starbucks_branch
        self.place = place
        self.names = []
        for i in names:
            self.names.append(i)

    def __len__(self):
        return len(self.names)

    def __add__(self, name):
        self.names.append(name)
        return self

    def __sub__(self, other):
        self.names.append(other)
        return self

    def showNamesInCoffee(self):
        print("Имя на кофе")
        print("------------")
        for name in self.names:
            if (len(name) > 5):
                print(name, " - ", name[0:5])
            else:
                print(name, " - ", name)

    def showNameInCoffee(self, name):
        if (len(name) > 5):
            print(name, " - ", name[0:5])
        else:
            print(name, " - ", name)


toktogula = Starbucks("Starbucks 1", "Toktogulova 102", "Ellen", "Barbara", "Duglas")
print(len(toktogula))
toktogula = toktogula + "Bambi"
toktogula.showNamesInCoffee()
toktogula.showNameInCoffee("Denzel")
