

class Human:
    def __init__(self, name, age, height, gender):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender

    def can_calculate(self, number_1, number_2):
        summary = number_1 + number_2
        return summary

    def can_say_hello(self):
        return "hello world"

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Age: {self.age}\n' \
               f'Height: {self.height}\n' \
               f'Gender: {self.gender}'

class Programmer(Human):
    def __init__(self, name, age, height, gender, language, fast_typing, logic_thinking):
        super().__init__(name, age, height, gender)
        self.language = language
        self.fast_typing = fast_typing
        self.logic_thinking = logic_thinking

    def can_freely_use_laptop(self):
        print("yeap, i can freely use laptop like a God")

    def __str__(self):
        return f'Language: {self.language}\n' \
               f'Fast Typing: {self.fast_typing}\n' \
               f'Logic Thinking: {self.logic_thinking}'

human_1 = Human(name="Aidana", age=18, height=170, gender="female")
human_2 = Human("Aelin", 20, 179, "female")

print(human_1.can_calculate(int(input("First:")), int(input("Second:"))))
print(human_1)
print(human_2)
print(human_2.can_say_hello())

proger = Programmer(language="Python",
                    fast_typing=True,
                    logic_thinking=True,
                    name="Aidana", age=18, height=170, gender="female")
print(proger)
