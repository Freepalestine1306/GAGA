print("Welcome user to calculator Python Edition")
Number1 = float(input("Enter your first number: "))
Number2 = float(input("Enter your second number: "))
Op = input("Enter the operation you want, For example: plus, minus, multiplacation, divsion: ")

if Op == "plus" or Op == '+':
    print("The answer for this equation is: ")
    print(Number1 + Number2)
elif Op == "minus" or Op == '-':
    print("The answer for this equation is: ")
    print(Number1 - Number2)
elif Op == "multiplacation" or Op == '*':
    print("The answer for this equation is: ")
    print(Number1 * Number2)
elif Op == "division" or Op == '/':
    print("The answer for this equation is: ")
    print(Number1 / Number2)
else :
    print("You did not enter a valid operation")
    print("Please try again")