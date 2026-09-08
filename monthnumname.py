month = input("Enter month name: ")
match month:
    case "January":
        print("1")
    case "February":
        print("2")
    case "March":
        print("3")
    case "April":
        print("4")
    case "May":
        print("5")
    case "June":
        print("6")
    case "July":
        print("7")
    case "August":
        print("8")
    case "September":
        print("9")
    case "October":
        print("10")
    case "November":
        print("11")
    case "December":
        print("12")
    case _:
        print("Invalid month")
