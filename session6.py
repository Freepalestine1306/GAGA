import turtle
import time
import random

t = turtle.Turtle()
t.hideturtle()
t.penup()

number = random.randint(1, 6)

colors = [
    "red" , "blue" , "green" , "yellow" , "purple" , "orange" , "pink" , "brown",
    "black" , "white" , "gray" , "cyan" , "magenta" , "gold" , "silver" , "navy",
    "skyblue" , "dodgerblue" , "royalblue" , "indigo" , "violet" , "plum" , "orchid",
    "lime" , "forestgreen" , "seagreen" , "springgreen" , "khaki" , "coral" , "tomato",
    "salmon" , "lightcoral" , "firebrick" , "crimson" , "sienna" , "chocolate",
    "saddlebrown" , "lightgray" , "darkgray" , "dimgray"
]

t.color(random.choice(colors))

t.clear()
time.sleep(1)
t.write(f"🎲 Dice: {number}", align="center", font=("Arial", 30, "bold"))
time.sleep(3)
