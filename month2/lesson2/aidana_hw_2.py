# No1
# 1. Создать трехступенчатую концепцию (дед-отец-ребенок) любого примера который вам ближе
# 2. Все три класса должны иметь свои особенные методы и атрибуты как минимум два доп метода у каждого класса
# 3. Также создать хотя бы по одному объекту к каждому классу

class Haikyu_1_season:
    def __init__(self, country, genre, kind_of_sport, team_name, official_color):
        self.country = country
        self.genre = genre
        self.kind_of_sport = kind_of_sport
        self.team_name = team_name
        self.official_color = official_color

    def winnings(self):
        return f"{self.team_name} has 3 wins in the first season"

    def __str__(self):
        return f"Country: {self.country}\n" \
               f"Genre: {self.genre}\n" \
               f"Kind of sport: {self.kind_of_sport}\n" \
               f"Team name: {self.team_name}\n" \
               f"Official color: {self.official_color}\n"


season1 = Haikyu_1_season(country="Japan", genre="sport, comedy", kind_of_sport="volleybal",
                          team_name="KARASUNO", official_color="black")

print(season1)
print(season1.winnings())
print("~" * 39)


class Haikyu_2_season(Haikyu_1_season):
    def __init__(self, country, genre, kind_of_sport, team_name, official_color, opposing_team, leader):
        super(Haikyu_2_season, self).__init__(country, genre, kind_of_sport, team_name, official_color)
        self.opposing_team = opposing_team
        self.leader = leader

    def winnings(self):
        return f"In the second season {self.team_name} defeated {self.opposing_team}"

    def __str__(self):
        return super(Haikyu_2_season, self).__str__() + f"Opposing team: {self.opposing_team}\n" \
                                                        f"Leader: {self.leader}\n"


season2 = Haikyu_2_season(country="Japan", genre="sport, comedy", kind_of_sport="volleybal",
                          team_name="KARASUNO", official_color="black",
                          opposing_team="Aobajohsai", leader="Sawamura Daichi")

print(season2)
print(season2.winnings())
print("~" * 49)


class Haikyu_3_season(Haikyu_2_season):
    def __init__(self, country, genre, kind_of_sport, team_name, official_color, opposing_team, leader,
                 friendly_match, new_manager):
        super(Haikyu_3_season, self).__init__(country, genre, kind_of_sport, team_name,
                                              official_color, opposing_team, leader)
        self.friendly_match = friendly_match
        self.new_manager = new_manager

    def winnings(self):
        return f"In the third season {self.team_name} won the {self.opposing_team}," \
               f"but lost to {self.friendly_match} in a friendly match"

    def __str__(self):
        return super(Haikyu_3_season, self).__str__() + f"Friendly match: {self.friendly_match}\n" \
                                                        f"New manager: {self.new_manager}\n"


season3 = Haikyu_3_season(country="Japan", genre="sport, comedy", kind_of_sport="volleybal",
                          team_name="KARASUNO", official_color="black",
                          opposing_team="Dateko", leader="Sawamura Daichi",
                          friendly_match="Nekoma high school", new_manager="Hitoka Yachi")

print(season3)
print(season3.winnings())
print("~" * 94)


# №2
# 1. Создать один класс в котором вы пропишете по одному методу (внутреннего и защищенного)
# 2. В этом классе должно быть также по одному атрибуту (внутреннего и защищенного)

class GeekTech:
    def _staff(self):
        print("Это внутренний метод объекта")
        print("=" * 94)

    def __founders(self):
        print("Это защищенный метод")

    def __init__(self):
        self.__founders = "Aidar, Nurgazy"
        self._mentor = "Mirhad"


courses = GeekTech()
courses._staff()
fnd = GeekTech()
#fnd.__founders()


# No3
# 1. Создать три разных класса в котором будут одинаковые методы по названию например (attack)
# 2. Но логика этого самого метода будут разные как в случае примера с мечником , лучником и волшебником

class Wolf:
    def eat(self):
        print("Wolf eating meat")


class Ram:
    def eat(self):
        print("Ram eating grass")


class Chimpanzee:
    def eat(self):
        print("Chimpanzee eating banana")

wolf = Wolf()
wolf.eat()

ram = Ram()
ram.eat()

makaka = Chimpanzee()
makaka.eat()
print("~" * 50)

# No4
# 1. Все тоже самое как в случае с Полиморфизмом без наследование , единственное различие здесь присутствует
# наследование трехступенчатой концепций (дед-отец-ребенок)

class Granny:
    def watch(self):
        print("Granny watching the news")


class Mother(Granny):
    def watch(self):
        print("Mother watching tv series")


class Daughter(Mother):
    def watch(self):
        print("Daughter watching a cartoon")

granny = Granny()
granny.watch()

mother = Mother()
mother.watch()

daughter = Daughter()
daughter.watch()

