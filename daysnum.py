day = int(input("Enter day number: "))
match day:
    case 1:
        print("M,T,W,T,F,S")
    case 2:
        print("T,W,T,F,S")
    case 3:
        print("W,T,F,S")
    case 4:
        print("T,F,S")
    case 5:
        print("F,S")
    case 6:
        print("S")
    case 7:
        print("No remaining days")
    case _:
        print("Invalid day")
