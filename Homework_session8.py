import time

while True:
    try:
        print("Hello user to word slicer")

        time.sleep(0.5)

        text = input("What is the text you want to slice: ")

        time.sleep(0.5)

        slicer1 = int(input("From where do you want to start the slice, enter the number you want to slice from begging by zero but spaces and everything counts: "))

        time.sleep(0.5)

        slicer2 = int(input("Enter where you want to end the slicer: "))

        slicer3 = slicer2+1

        if slicer1 == 0:

            time.sleep(0.5)

            print(text[0 : slicer3])

        else:

            time.sleep(0.5)

            print(text[slicer1 : slicer3])

        again = input("Do you want to try again? ")

        if again.lower() != "yes" and again.lower() != "y":
            break

    except ValueError:
        print("You entered something that's not a valid number")

        try_again = input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except NameError:
        print("You used a name that doesn't exist")

        try_again = input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except TypeError:
        print("You used the wrong type of value")

        try_again = input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except IndexError:
        print("That's out of range")

        try_again = input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except KeyError:
        print("That key doesn't exist")

        try_again = input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except ZeroDivisionError:
        print("You can't divide by zero")

        try_again = input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except FileNotFoundError:
        print("You entered a file that does not exist")

        try_again = input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except AttributeError:
        print("That doesn't work on that type of value")

        try_again = input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break
