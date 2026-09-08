month = int(input("Enter month number: "))
match month:
    case 1:
        print("31 DAYS")
    case 2:
        print("28 OR 29 DAYS")
    case 3:
        print("31 DAYS")
    case 4:
        print("30 DAYS")
    case 5:
        print("31 DAYS")
    case 6:
        print("30 DAYS")
    case 7:
        print("31 DAYS")
    case 8:
        print("31 DAYS")
    case 9:
        print("30 DAYS")
    case 10:
        print("31 DAYS")
    case 11:
        print("30 DAYS")
    case 12:
        print("31 DAYS")
    case _:
        print("Invalid month")
