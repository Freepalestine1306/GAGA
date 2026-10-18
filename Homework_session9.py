import time

while True:
    try:

        print("hello user to nested loop python printer")

        time.sleep(0.5)

        printy = input("What is the thing you want to repeat it: ")

        time.sleep(0.5)

        repeat = int(input("How much times do you want it to be printed: "))

        pattern = input("Do you want to make a pattern: ")

        pattern.upper()

        time.sleep(0.5)

        if pattern == "NO":

            for i in range(repeat):

                print(printy, end=" ")

                time.sleep(1)

                print("\n")

        elif pattern == "YES":

            for i in range(repeat):
                 j=0

                 while j<=i:

                     print(printy, end=" ")

                     time.sleep(0.5)

                     j+=1

                     print("\n")

        again = input("Do you want to try again? ")

        if again.lower() != "yes" and again.lower() != "y":
            break

    except ValueError:
        print("you entered something that's not a valid number")

        try_again = input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except NameError:
        print("you used a name that doesn't exist")

        try_again = input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except TypeError:
        print("you used the wrong type of value")

        try_again = input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except IndexError:
        print("that's out of range")

        try_again = input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except KeyError:
        print("that key doesn't exist")

        try_again = input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except ZeroDivisionError:
        print("you can't divide by zero")

        try_again = input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except FileNotFoundError:
        print("you entered a file that does not exist")

        try_again = input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except AttributeError:
        print("that doesn't work on that type of value")

        try_again = input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break
