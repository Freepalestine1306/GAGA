import time
while True:

    print("Welcome user to calculator Python Edition")
    time.sleep(0.5)
    Number1 = float(input("Enter your first number: "))
    time.sleep(0.5)
    Number2 = float(input("Enter your second number: "))
    time.sleep(0.5)
    Op = input("Enter the operation you want, For example: plus, minus, multiplacation, divsion: ")
    time.sleep(0.5)

    if Op == "plus" or Op == '+':
        print("The answer for this equation is: ")
        time.sleep(1)
        print(Number1 + Number2)
    elif Op == "minus" or Op == '-':
        print("The answer for this equation is: ")
        time.sleep(1)
        print(Number1 - Number2)
    elif Op == "multiplacation" or Op == '*':
        print("The answer for this equation is: ")
        time.sleep(1)
        print(Number1 * Number2)
    elif Op == "division" or Op == '/':
        print("The answer for this equation is: ")
        time.sleep(1)
        print(Number1 / Number2)
    else :
        print("You did not enter a valid operation")
        time.sleep(1)

    Again = input("Do you want to try again: ")

    if Again == "No" or Again == "no" or Again == "NO":
        time.sleep(0.5)
        print("Thank you for using calculator Python Edition")
        time.sleep(0.5)
        print("Goodbye!")
        time.sleep(0.5)
        break