opinion = input("enter your opinion, do you want to stay in the house or go outside")
place = input("enter your favourite place")
food = input("If you are going to stay at home what food are you going to order")

if opinion == "stay":
    if food == "pizza":
        print("ordering pizza")
    elif food == "kabsah":
        print("Make the kabsah at home")
elif opinion == "go outside":
    if place == "zoo":
        print("go to the zoo and take a picture with a lion")
    elif place == "park":
        print("go to the park play on the trampoline")