def zodiak_signs(day, month, name="Aidana"):
    print(name, end=', ')

    if 21 <= day < 32 and month == 3 or day <= 20 and month == 4:
        print(name, "овен")
    if 21 <= day < 31 and month == 4 or day <= 21 and month == 5:
        print("телец")
    if 22 <= day < 32 and month == 5 or day <= 21 and month == 6:
        print("близнецы")
    if 22 <= day < 31 and month == 6 or day <= 22 and month == 7:
        print("рак")
    if 23 <= day < 32 and month == 7 or day <= 21 and month == 8:
        print("лев")
    if 22 <= day < 32 and month == 8 or day <= 23 and month == 9:
        print("дева")
    if 24 <= day < 31 and month == 9 or day <= 23 and month == 10:
        print("весы")
    if 24 <= day < 32 and month == 10 or day <= 23 and month == 11:
        print("скорпион")
    if 24 <= day < 31 and month == 11 or day <= 22 and month == 12:
        print("стрелец")
    if 23 <= day < 32 and month == 12 or day <= 20 and month == 1:
        print("козерог")
    if 21 <= day < 32 and month == 1 or day <= 19 and month == 2:
        print("водолей")
    if 20 <= day < 29 and month == 2 or day <= 20 and month == 3:
        print("рыбы")


zodiak_signs(99, 10)
