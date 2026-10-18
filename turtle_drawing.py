import turtle

from slow_print import slow_print

from slow_print import slow_input

import time


try:

    slow_print("Welcome to the turtle program")

    drawing = slow_input("What Do you want to draw? ")

    drawing = drawing.lower()

    t = turtle.Turtle()

    size = slow_input("What size do you want your drawing to be? eg: small, medium, large ")

    color = slow_input("What color do you want your drawing to be? ")

    size2 = int(slow_input("What do you want the size of the pen to be? "))

    speed = int(slow_input("What do you want the speed of the mouse to be? (1-10) "))

    size = size.lower()

    color = color.lower()

    t.color(color)

    t.speed(speed)

    t.pensize(size2)

    t.pendown()

slow_print("Welcome to the turtle program")

drawing = slow_input("What Do you want to draw? ")

drawing = drawing.lower()

t = turtle.Turtle()

size = slow_input("What size do you want your drawing to be? eg: small, medium, large ")

color = slow_input("What color do you want your drawing to be? ")

size2 = int(slow_input("What do you want the size of the pen to be? "))

speed = int(slow_input("What do you want the speed of the mouse to be? (1-10) "))

size = size.lower()

color = color.lower()

t.color(color)

t.speed(speed)

t.pensize(size2)

t.pendown()

if drawing == "square":

    for i in range(4):

        if size == "small":

            t.forward(50)
                
            time.sleep(0.5)

            t.right(90)
            
        elif size in ["medium", "normal"]:
                
            t.forward(100)
                
            time.sleep(0.5)

            t.right(90)

        elif size in ["large", "big"]:

            t.forward(150)

            time.sleep(0.5)

            t.right(90)

elif drawing == "circle":  

    if size == "small":

        t.circle(50)

    elif size in["medium", "normal"]:
            
         t.circle(100)

    elif size in ["large", "big"]:

        t.circle(150)

elif drawing == "triangle":

    for i in range(3):

        if size == "small":

            t.forward(50)

            time.sleep(0.5)

            t.right(120)

        elif size in ["medium", "normal"]:
                
            t.forward(100)

            time.sleep(0.5)

            t.right(120)

        elif size in["large", "big"]:

            t.forward(150)

            time.sleep(0.5)

            t.right(120)

elif drawing == "star":

    for i in range(5):

        if size == "small":

            t.forward(50)

            time.sleep(0.5)

            t.right(144)

        elif size in ["medium", "normal"]:

            t.forward(100)

            time.sleep(0.5)

            t.right(216)

        elif size in ["large", "big"]:

            t.forward(150)

            time.sleep(0.5)

            t.right(288)

elif drawing == "rectangle":

    for i in range(2):

        if size == "small":

            t.forward(50)

            time.sleep(0.5)

            t.right(90)

        elif size in ["medium", "normal"]:

            t.forward(100)

            time.sleep(0.5)

            t.right(90)

except NameError:

    slow_print("You have entered an invalid input.")

    again = slow_input("Do you want to try again? (yes/no) ")

    if again.lower() in ["yes", "y"]:

        subprocess.run(["python", "turtle_drawing.py"])

    elif again.lower() in ["no", "n"]:
        
        slow_print("Thank you for using the turtle program")

        time.sleep(1)

        slow_print("Goodbye!")

        exit()

    else:
        slow_print("You did not enter a valid answer")

        time.sleep(1)

        slow_print("Thank you for using the turtle program")

        time.sleep(1)

        exit()