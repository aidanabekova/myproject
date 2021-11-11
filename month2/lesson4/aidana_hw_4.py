# Задание No 1
# 1. Создать класс TimeDesk , в котором будет один атрибут seconds
# 2. Надо в методе продумать логику конвертера секунд на дни , часы ,
# минуты и секунды
# 3. Если было дано 70 секунд то вывод должен быть 0 дней, 0 часов , 1
# минута , 10 секунд
# 4. Если было дано 86401 секунда то вывод должен быть 1 день , 0 часов
# , 0 минут и 1 секунда

class TimeDesk:
    def __init__(self, seconds):
        self.seconds = seconds

    def show_time(self):
        years = int(self.seconds / (365 * 24 * 60 * 60))
        self.seconds -= years * 365 * 24 * 60 * 60
        month = int(self.seconds / (31 * 24 * 60 * 60))
        self.seconds -= month * 31 * 24 * 60 * 60
        days = int(self.seconds / (24 * 60 * 60))
        self.seconds -= days * 24 * 60 * 60
        hours = int(self.seconds / 60 / 60)
        self.seconds -= hours * 60 * 60
        minutes = int(self.seconds / 60)
        self.seconds -= minutes * 60
        return f"{years} years, {month} month, {days} days, {hours} hours, {minutes} minutes, {self.seconds} seconds"

    def show_your_time(self):
        seconds = int(input("Enter the number of seconds: "))
        d = TimeDesk(seconds)
        return d.show_time()

    def __str__(self):
        return f"Seconds: {self.seconds}\n"


t = TimeDesk(1000)

print(t.show_your_time())


# Задание No 2
# 1. Создать любой класс который вам по душе
# 2. Прописать Метод для @property @classmethod @staticmethod
# 3. Использовать декоратор @property и обратить метод в setter и deleter,
# также попробовать внести изменения
# 4. Использовать @classmethod и попробовать обратиться к нему и
# изменить его значение
# 5. Использовать @staticmethod и прописать любую функцию
# независимого от класса


class Aidana:
    def __init__(self, name, surname, zodiac_sign):
        self.name = name
        self.surname = surname
        self.zodiac_sign = zodiac_sign

    @property
    def full_information(self):

        info = self.surname + " " + self.name + " " + self.zodiac_sign
        return info

    @full_information.setter
    def full_information(self, info):
        self.name, self.surname, self.zodiac_sign = info.split()

    @full_information.deleter
    def full_information(self):
        self.surname = None
        self.name = None
        self.zodiac_sign = None
        print("Full information deleted! ")

    def __str__(self):
        return f"Name: {self.name}\n"\
               f"Surname: {self.surname}\n"\
               f"Zodiac sign: {self.zodiac_sign}\n"


bab = Aidana(name="Aidana", surname="Bekova", zodiac_sign="Libra")

print(bab)
print(bab.full_information)
bab.full_information = "Agnia Adykeeva sagittarius"
print(bab.full_information)
#del bab.full_information
print(bab.full_information)
#bab.full_information = "Aidana Bekova vesi"
print(bab.full_information)

class AidanasAge():
    @staticmethod
    def age(age):
        if age >= 18:
            return True
        else:
            return False

print("~" * 30)
print(AidanasAge.age(18))

