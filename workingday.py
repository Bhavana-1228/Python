day = int(input("Enter day number: "))
match day:
    case 1:
        print("Sunday is not a working day")
    case 2:
        print("Monday is a working day")
    case 3:
        print("Tuesday is a working day")
    case 4:
        print("Wednesday is a working day")
    case 5:
        print("Thursday is a working day")
    case 6:
        print("Friday is a working day")
    case 7:
        print("Saturday is not a working day")
    case _:
        print("Invalid day")
