Osh = float(input("Температура в Оше:"))
Chui = float(input("Температура в Чуе:"))
Naryn = float(input("Температура в Нарыне:"))
Batken = float(input("Температура в Баткене:"))
JB = float(input("Температура в JB: "))
IK = float(input("Температура на IK:"))
Talas = float(input("Температура в Таласе:"))

average = (Osh+Chui+Naryn+Batken+JB+IK+Talas)/7
average = round(average, 2)
print("Средний показатель температуры по Кыргызстану на сегодня", average, "℃")
