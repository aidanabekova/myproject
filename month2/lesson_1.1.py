class Car:
    def __init__(self, brand, color, type_car, amount_passenger, max_speed,
                engine, country, year, mechanic):
        if isinstance(brand, str):
            self.brand = brand
        else:
            raise ValueError("Brand should be string!")
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError("Color should be string")
        if isinstance(type_car, str):
            self.type_car = type_car
        else:
            raise ValueError("Type car should be string")
        if isinstance(amount_passenger, int):
            self.amount_passenger = amount_passenger
        else:
            raise ValueError("Amount passenger should be integer")
        if isinstance(max_speed, int):
            self.max_speed = max_speed
        else:
            raise ValueError("Max speed should be integer")
        if isinstance(engine, float):
            self.engine = engine
        else:
            raise ValueError("Engine should be float")
        if isinstance(country, str):
            self.country = country
        else:
            raise ValueError("Country should be string")
        if isinstance(year, int):
            self.year = year
        else:
            raise ValueError("Year should be integer")
        if isinstance(mechanic, str):
            self.mechanic = mechanic
        else:
            raise ValueError("Mechanic should be string")

    def tunning(self, cost):
        car_cost = 1000
        summary = car_cost + cost
        return summary

    def __str__(self):
        return f'{self.brand}, {self.color}, {self.type_car}, {self.amount_passenger}, {self.max_speed},' \
               f' {self.engine}, {self.country}, {self.year}, {self.mechanic}'



car_1 = Car(brand = "bmw", color = "black", year = 2021, country = "Germany", amount_passenger = 4, max_speed = 360,
            type_car = "Crossover", engine = 6.0, mechanic = "Nope")

print(car_1)
print(car_1.tunning(80000))
