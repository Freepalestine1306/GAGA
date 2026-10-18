import time
from slow_print import slow_print, slow_input

while True:
    try:
        slow_print("Hello Consumer")

        time.sleep(0.5)

        listt = []

        items = int(slow_input("How many things did you buy: "))

        time.sleep(0.5)

        i = 1
        j = 0
        while items >= i:

            price = float(slow_input(f"How much is your {i} item: "))

            time.sleep(0.5)

            listt.append(price)

            i += 1

        total = 0

        while True:
            tax = slow_input("Do you want to add tax? ")

            if tax == "yes" or tax == "Yes" or tax == "YES" or tax == "y" or tax == "Y":

                tax2 = float(slow_input("How much is the tax? "))

                for p in range(len(listt)):

                    total+=listt[p]

                total*=tax2

                break

            elif tax == "No" or tax == "NO" or tax == "N" or tax == "n" or tax == "no":

                for p in range(len(listt)):

                    total+=listt[p]

                break

            else:
                slow_print("You did not enter a answer")

                try_again = slow_input("Do you want to try again? ")

                if try_again.lower() != "yes" and try_again.lower() != "y":
                    exit()

        time.sleep(0.5)

        slow_print(f"The total is : {total}")

        again = slow_input("Do you want to try again? ")

        if again.lower() != "yes" and again.lower() != "y":
            break

    except ValueError:
        slow_print("You entered something that's not a valid number")

        try_again = slow_input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except NameError:
        slow_print("You used a name that doesn't exist")

        try_again = slow_input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except TypeError:
        slow_print("You used the wrong type of value")

        try_again = slow_input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except IndexError:
        slow_print("That's out of range")

        try_again = slow_input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except KeyError:
        slow_print("That key doesn't exist")

        try_again = slow_input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except ZeroDivisionError:
        slow_print("You can't divide by zero")

        try_again = slow_input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except FileNotFoundError:
        slow_print("You entered a file that does not exist")

        try_again = slow_input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except AttributeError:
        slow_print("That doesn't work on that type of value")

        try_again = slow_input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break
