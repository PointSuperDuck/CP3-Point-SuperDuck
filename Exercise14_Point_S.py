def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "point" and passwordInput == "9466":
        return showMenu()
    else:
        print("Try Again!")
def showMenu():
    print("--------iShop---------")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("9. Done!")
    return menuSelect()
def menuSelect():
    userSelected = 0
    while userSelected != 9:
        userSelected = int(input("Please Select Menu>>"))
        if userSelected == 1:
            vatCalculate(totalPrice=int(input("Price(THB) : ")))
        elif userSelected == 2:
            priceCalculate()
    print("Done "+"Thank you! :)")
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return print(result,"(THB)")
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return print(vatCalculate(price1+price2),"(THB)")

login()