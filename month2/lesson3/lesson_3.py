# магические методы в классах и множественное наследование
class Tarif:
    def __init__(self, number, name, summary):
        self.number = number
        self.name = name
        self.summary = summary

    def cal(self):
        return f"This is number: {self.number}, can call but with restriction"

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Number: {self.number}\n" \
               f"Summary: {self.summary}"


number1 = Tarif(name="Adilet", number="0774446852", summary="120")
#print(number1)


class UnlCallTarif(Tarif):

    def unl_call(self):
        return f"This number: {self.number}, can call but without restriction"

    def __str__(self):
        return super(UnlCallTarif, self).__str__()


number2 = UnlCallTarif(name="Aelina", number="0774578675", summary="1500")
# print(number2)


class UnlInternetTarif(Tarif):
    def unl_internet(self):
        return f"your Internet package is unlimited"

    def __str__(self):
        return super(UnlInternetTarif, self).__str__()


number3 = UnlInternetTarif(name="Georg",
                           number="0777123456",
                           summary=4000)
#print(number3)


class DiamondTarif(UnlCallTarif, UnlInternetTarif):
    def __str__(self):
        return super(DiamondTarif, self).__str__()


diamond = DiamondTarif(name="Alex",
                       number="0777888888",
                       summary=12000)
print(diamond.unl_call())
print(diamond.unl_internet())
print(diamond)