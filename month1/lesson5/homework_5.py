#a)
def rectangle(height, width):
    return float(height * width)
result = rectangle(5, 3)
print(result)

#b)
def numbers (*a):
    return sum(a)//len(a)
print(numbers(56,43,2,1,10))

#c)
def menu(breakfast, lunch, dinner):
    return{"завтрак": breakfast, "обед": lunch, "ужин": dinner}
monday = menu("сырники", "стейк", "суп")
tuesday = menu("каша", "котлеты с пюре", "салат")
print(monday)
print(tuesday)