
class Animal:
    def __init__(self, color, name, detachment, age, gender):
        self.color = color
        self.name = name
        self.detachment = detachment
        self.age = age
        self.gender = gender


    def __str__(self):
        return f'Color: {self.color}\n' \
               f'Name: {self.name}\n' \
               f'Detachment: {self.detachment}\n' \
               f'Age: {self.age}\n' \
               f'Gender:{self.gender}'


animal1 = Animal("orange", "lion", "predator", 3, "male")
animal2 = Animal("multicolored", "parrot", "booty", 18, "male")
animal3 = Animal("brown", "monkey", "predator", 12, "female")

class Zoo(Animal):
    def __init__(self, color, detachment, age, gender, action, habitat, country, weight, name):
        super().__init__(color, name, detachment, age, gender)
        self.action = action
        self.habitat = habitat
        self.country = country
        self.weight = weight
    def __str__(self):
        return super().__str__()+f'\n' \
               f'Action: {self.action}\n' \
               f'Habitat: {self.habitat}\n' \
               f'Country: {self.country}\n' \
               f'Weight: {self.weight}\n'


zoopark1 = Zoo("orange",  "predator", 3, "male", "stands on two legs and jumps", "cell", "Africa", "150kg", name="lion")
zoopark2 = Zoo("multicolored", "booty", 18, "male", "flies and sings", "artificial_trees",
               "Australia", "12kg", name="parrot")
zoopark3 = Zoo("brown", "predator", 12, "female", "dancing and doing somersaults", "artificial_forest",
               "China", "45kg", name="monkey")

class Zoo_show:
    def __init__(self, zoo):
        self.zoo = zoo
        self.ticket = 0

        if (zoo.name == "lion"):
            self.ticket = '50$'
        if (zoo.name == "parrot"):
            self.ticket = '40$'
        if (zoo.name == "monkey"):
            self.ticket = '20'

    def tickete(self):
        return "The cost of the show will be: " + self.ticket

    def __str__(self):
        return f'{self.zoo.name} will show {self.zoo.action}'


show1 = Zoo_show(zoopark1)
show2 = Zoo_show(zoopark2)
show3 = Zoo_show(zoopark3)

print(show1)
print(show1.tickete())

print(show2)
print(show2.tickete())

print(show3)
print(show3.tickete())










