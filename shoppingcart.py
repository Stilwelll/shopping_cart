from audioop import add
from timeit import repeat
from tkinter import W, Y
from unicodedata import name

shopping_cart = {"Name": [], "Price": [], "Quantity": []}


def main():
    active = "y"
    while active == "y":
        shopping_cart["Name"].append(
            input("What is the Name of the Item you like to add?: "))
        try:
            shopping_cart["Price"].append(int(input("What is the Price of this item?: ")))
        except ValueError:
            print("Only Integers may be entered has a price. Please try again.")
            main()
        try:
            shopping_cart["Quantity"].append(int(input("How many would you like to buy?: ")))
        except ValueError:
            print("Only Integers may be entered has the quantity. Please try again.")
            main()
        active = input("Would you like to add another item?(y/n): ")
        if active == "n":
            break
        while "y" not in active:
            active = input(
                "That was an Invalid input, please enter y (Yes) or n (No) to continue: ")
            if active == "n":
                break
    choice()


def choice():
    choice = ""
    choice = input("Would you like to Add an item? Delete an Item? Check what you have? or Exit and get your Receipt?(Options: add/delete/check/get receipt): ")
    if choice == "add":
        main()
    elif choice == "delete":
        delete()
    elif choice == "check":
        check()
    elif choice == "get receipt":
        get_receipt()
    while "get receipt" or "check" or "delete" or "add" not in choice:
        choice = input("Invalid Option. Please pick from these options. (Options: add/delete/check/get receipt): ")
        if choice == "add":
            break
        elif choice == "delete":
            break
        elif choice == "check":
            break
        elif choice == "get receipt":
            break
    if choice == "add":
        print("hi")
    elif choice == "delete":
        delete()
    elif choice == "check":
        check()
    elif choice == "get receipt":
        get_receipt()


def delete():
    item_name = input("What item would you like to delete?: ")
    del shopping_cart["Name"]
    item_price = input("What was the items price?: ")
    del shopping_cart["Price"]
    item_quantity = input("How much of it would you like to delete?: ")
    del shopping_cart["Quantity"]
    choice()


def check():
    print(
        f"You Current Have: {shopping_cart['Name']}. Then each costed this much: {shopping_cart['Price']}, you have this much of them: {shopping_cart['Quantity']}")
    choice()


def get_receipt():
    total_price = shopping_cart["Price"].copy() 
    total_amount = shopping_cart["Quantity"].copy() 
    num = sum(total_price)
    num1 = sum(total_amount)
    num *= num1
    print(f"Your Total is {num} Dollars. You have {shopping_cart['Quantity']} Units of {shopping_cart['Name']}.\nThank you for using this program!")


main()
