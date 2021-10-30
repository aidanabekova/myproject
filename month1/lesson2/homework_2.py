while True:
    code = input("Enter region code:")

    if code == "01" or code == "1":
        print("Bishkek city")
    elif code == "02" or code == "2":
        print("Osh city")
    elif code == "03" or code == "3":
        print("Batken")
    elif code == "04" or code == "4":
        print("Dzhalal-Abad")
    elif code == "05" or code == "5":
        print("Naryn")
    elif code == "06" or code == "6":
        print("Osh")
    elif code == "07" or code == "7":
        print("Talas")
    elif code == "08" or code == "8":
        print("Chui")
    elif code == "09" or code == "9":
        print("Issyk-Kul")
    elif code == "0" or code == "выйти":
        print("Выход из цикла")
        break
    else:
        print("Ошибка,повторите попытку!")
