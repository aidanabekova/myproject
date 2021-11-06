# class Wizard:
#     def __init__(self, name, ticket):
#         self.name = name
#         self.ticket = ticket
#
#     def __add__(self, other):
#         print("1. Fire ball")
#         print("2. Freeze spell")
#         if self.ticket == 1:
#             summary = other + self.ticket
#             return summary
#         elif self.ticket == 2:
#             summary = other + self.ticket
#             return summary
#
#     def __str__(self):
#         return f"{self.name}, {self.ticket}"
#
#     def __len__(self):
#         return len(self.name)
#
#
# wiz = Wizard(name="Gendelf", ticket=2)
# print(wiz.__add__(200))
# print(wiz.__str__())
# print(wiz.__len__())

class Human:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f"{self.first}{self.last}.@gmail.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    def __str__(self):
        return f"{self.first} {self.last}"

h = Human(first="Liz", last="Wizardo")
print(h)
print(h.fullname)

