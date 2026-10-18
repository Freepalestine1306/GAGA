import turtle
import time
import random

t = turtle.Turtle()

colors = [
    "red" , "blue" , "green" , "yellow" , "purple" , "orange" , "pink" , "brown",
    "black" , "gray" , "cyan" , "magenta" , "gold" , "silver" , "navy",
    "skyblue" , "dodgerblue" , "royalblue" , "indigo" , "violet" , "plum" , "orchid",
    "lime" , "forestgreen" , "seagreen" , "springgreen" , "khaki" , "coral" , "tomato",
    "salmon" , "lightcoral" , "firebrick" , "crimson" , "sienna" , "chocolate",
    "saddlebrown" , "lightgray" , "darkgray" , "dimgray"
]


t.speed(5)

while True:
    try:
        for i in range(5):
            t.font = ("Arial", 30, "bold")
            t.pencolor(random.choice(colors))
            t.forward(150)
            t.right(144)
            t.pendown()

        time.sleep(2)

        for i in range(1):
            t.penup()
            t.pencolor(random.choice(colors))
            t.goto(-160, 100)
            t.pendown()
            t.circle(200)
            time.sleep(4)
            t.pendown()


        time.sleep(2)

        again = input("Do you want to try again? ")

        if again.lower() != "yes" and again.lower() != "y":
            break

        t.reset()

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
