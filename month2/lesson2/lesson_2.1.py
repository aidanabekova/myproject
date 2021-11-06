# основные принципы ООП(Абстарция).Наследование.Инкапсуляция.Полиморфизм.
class Panda:
    def __init__(self, name, weight, color, fur):        #это пример полиморфизма
        self.name = name
        self.weight = weight
        self.color = color
        self.fur = fur

    def style_kung_fu(self):
        style = f"Dragon warrior, cause I'm {self.name}"
        return style

    def __str__(self):
        return f"Name: {self.name}\n" \          
               f"Weight: {self.weight}\n" \
               f"Color: {self.color}\n" \
               f"Fur: {self.fur}"


panda = Panda(name="Po",
              weight=200,
              color="black and white",
              fur=True)
print(panda)
print(panda.style_kung_fu())


class Tiger:
    def __init__(self, name, weight, color, fur):
        self.name = name
        self.weight = weight
        self.color = color
        self.fur = fur

    def style_kung_fu(self):
        style = f"\nTiger style, cause I'm {self.name}"
        return style

    def __str__(self):
        return f"\nName: {self.name}\n" \
               f"Weight: {self.weight}\n" \
               f"Color: {self.color}\n" \
               f"Fur: {self.fur}"


tiger1 = Tiger(name="Тигрица",
               weight=100,
               color="brown and black",
               fur=True)
print(tiger1.style_kung_fu())
print(tiger1)
