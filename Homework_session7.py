import time
import random

while True:
    try:
        questions = {0}

        print("Welcome user to get your info ")

        time.sleep(0.5)

        question1 = input("What is your name: ")

        time.sleep(0.5)

        while True:
            question2 = int(input("How old are you: "))

            time.sleep(0.5)

            if question2 <9:
                print("You are too young")

                try_again = input("Do you want to try again? ")

                if try_again.lower() != "yes" and try_again.lower() != "y":
                    exit()
            else:
                break


        question3 = input("Where do you live: ")

        time.sleep(0.5)


        if 15 <= question2 <= 65:

            question4 = input("What do you work: ")

            time.sleep(0.5)

            questions.add("Work: " + question4)

            if question4.lower() == "police":

                print("You work with the government\n")

                time.sleep(0.5)
            else:

                print("You don't work with the government")

                time.sleep(0.5)

        questions.add("Country: " + question3)


        questions.add("Age: " + str(question2))


        questions.add("Name: " + question1)


        questions.remove(0)

        time.sleep(0.5)

        "\n"

        for question in questions:
            print(question, "\n")
            time.sleep(1)

        print("Thanks for the info\n")

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
