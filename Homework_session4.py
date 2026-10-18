import time


def plus(numbers):
    return sum(numbers)


def minus(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result -= n
    return result


def multi(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result


def divi(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result /= n
    return result


def ask_try_again():
    while True:
        again = input("Do you want to try again: ").strip().lower()

        if again in ("no", "n"):
            time.sleep(0.5)
            print("Thank you for using calculator Python Edition")
            time.sleep(1)
            print("Goodbye!")
            time.sleep(1)
            return False

        if again in ("yes", "y"):
            return True

        print("You did not enter a correct answer")
        time.sleep(1)


while True:
    print("Welcome user to calculator Python Edition")
    time.sleep(0.5)

    try:
        howmany = int(input("How many numbers do you want to operate: "))

        time.sleep(0.5)

        if howmany < 1:
            print("Please enter at least 1 number")
            time.sleep(1)
            continue

        numbers = []
        for i in range(howmany):
            numbers.append(float(input(f"Enter number {i + 1}: ")))
            time.sleep(0.5)

        Op = input("Enter the operation you want, for example: plus, minus, multiplication, division: ").strip().lower()
        time.sleep(0.5)

    except ValueError:
        print("You did not enter a valid number")
        time.sleep(1)
        if not ask_try_again():
            break
        continue

    if Op in ("plus", "+"):
        print("The answer for this equation is: ")
        time.sleep(1)
        print(plus(numbers))
        time.sleep(0.5)

    elif Op in ("minus", "-"):
        print("The answer for this equation is: ")
        time.sleep(1)
        print(minus(numbers))
        time.sleep(0.5)

    elif Op in ("multiplication", "*"):
        print("The answer for this equation is: ")
        time.sleep(1)
        print(multi(numbers))
        time.sleep(0.5)

    elif Op in ("division", "/"):
        print("The answer for this equation is: ")
        time.sleep(1)
        try:
            print(divi(numbers))
        except ZeroDivisionError:
            print("Can't divide by zero")
        time.sleep(0.5)

    else:
        print("You did not enter a valid operation")
        time.sleep(1)

    if not ask_try_again():
        break
