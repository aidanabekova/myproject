#задание No1
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

    def __str__(self):
        return f"Name: {self.name}\n"\
               f"OOP: {self.OOP}\n"\
               f"Year of issue: {self.year_of_issue}\n"\
               f"Developer: {self.developer}\n"

language1 = C(name="language C",
              OOP=True, year_of_issue=1969-1973,
              developer="Dennis Ritchie")
print(language1)
print(language1.application())
print("~" * 163)


class Cpp(C):

    def application(self):
        return f"{self.name} is used in all areas of programming:" \
               f"from high-load systems to microcontroller programming"

    def __str__(self):
        return super(Cpp, self).__str__()

language2 = Cpp(name="languahe Cpp", OOP=True,
                year_of_issue=1985, developer="Bjorn Stroustrup")


