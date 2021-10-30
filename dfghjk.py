class Date():
    month = ["январь", "февраль"]
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.month_name = Date.month[month-1]




