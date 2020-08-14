price1 =50
price2 =60
usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "point" and passwordInput == "9466":
    print("Successful!")
    print("------Welcome to PoinTang Shop-------")
    print("     1. Esspresso         :50 THB")
    print("     2. Green Tea         :60 THB")
    print("-------Pls Select Product No.--------")
    userSelected = int(input("Drink No.>>"))
    if userSelected == 1:
        print("1. Esspresso         :50 THB")
        Drink = int(input("How many?>>"))
        if int(Drink):
            print("Total :", price1 * Drink, "THB")
    elif userSelected == 2:
        print("2. Green Tea         :60 THB")
        Drink = int(input("How many?>>"))
        if int(Drink):
            print("Total :", price2 * Drink, "THB")
else:
    print("Try again!")