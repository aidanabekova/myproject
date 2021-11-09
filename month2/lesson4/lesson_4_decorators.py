class Wizard:
    def __init__(self, first, last, ):
        self.first = first
        self.last = last

    def emailing(self):
        email = f"{self.first}.{self.last}@gmail.com"
        return email

    @staticmethod
    def add_some():
        summary = 1 + 2
        return summary

    @property
    def fullname(self):
        name = self.first + " " + self.last
        return name

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split()

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print("Fullname deleted!")

    def __str__(self):
        return f"Fullname: {self.first} {self.last}"


waz = Wizard(first="Liz", last="Wizardovna")

print(waz)
print(waz.fullname)
print(waz.emailing())
waz.first = "Aelin"
print(waz.fullname)
del waz.fullname
print(waz.fullname)
