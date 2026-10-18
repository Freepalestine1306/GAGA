import turtle
import time
import os

t = turtle.Turtle()

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def slow_input(prompt, delay=0.03):
    for char in prompt:
        print(char, end="", flush=True)
        time.sleep(delay)
    return input()

def draw_stars(count):
    for s in range(count):
        t.begin_fill()
        for i in range(5):
            t.forward(40)
            t.right(144)
        t.end_fill()
        t.penup()
        t.forward(60)
        t.pendown()



def trys():

    while True:
        again = slow_input("Do you want to go back to the menu? (y/n) ")

        if again.lower() == "y" or again.lower() == "yes":

            slow_print("Going back to the menu")

            break

        else:


            slow_print("Thank you for using our system\n\nBye!!")

            exit()


students = []

saved = 0

t = turtle.Turtle()

names = set()

subjects = ("Math", "English", "Science")



while True:

    while True:

        try:
            slow_print("===== Student Management System ===== ")

            opt = slow_input("Pick an option:\n1. Add more than one Student\n2. Show All Students\n3. Search for Student\n4. Show Statistics\n5. Save Students\n6. Load Students\n7. Draw Results\n8. Show names\n9. Exit\n10. Add one student\n11. Show subjects\n12. Show how much students are there\n13. Delete a student\n")

            opt = opt.lower()


            if opt == "1" or opt == "add more than one student":

                num = int(slow_input("How many students do you want to add? "))
                
                    
                
                for i in range(1, num+1):
                
                    name = slow_input(f"Enter the student number {i} name: ")
                
                    age = float(int(slow_input(f"Enter the student number {i} age: ")))

                    if age == 0 or age < 0:

                        slow_print("The students age isnt correct")

                        break

                    grade = int(slow_input(f"Enter the student number {i} grade: "))
                
                    math = float(slow_input(f"Enter the student number {i} grade for math out of 100%: "))
                
                    english = float(slow_input(f"Enter the student number {i} grade for english out of 100%: "))
                
                    science = float(slow_input(f"Enter the student number {i} grade for science out of 100%: "))
                
                    if math > 100 or english > 100 or science > 100 or math < 0 or english < 0 or science < 0:

                        slow_print("The marks must be between 0 and 100")

                        break
                
                    else:
                
                        average = math + english + science
                        
                
                    if average == 0:
                
                        average = 0
                
                    else:
                            
                        average = average/3
                    
                    
                    if average >= 90:

                        rating = "perfect"

                    elif 80 <= average < 90:

                        rating = "very good"

                    elif 70 <= average < 80:

                        rating = "good"

                    else:

                        rating = "bad"


                    names.add(name)

                    student = {"Name": name, "Age": age, "Math": math, "English": english, "Science": science, "Grade": grade, "Average": average, "Rating": rating}
            
                    students.append(student)

                trys()
        
            elif opt == "2" or opt == "show all students":
            
                    for student in students:
                        slow_print(f"Name: {student['Name']}\n")
                        slow_print(f"Age: {student['Age']}\n")
                        slow_print(f"Grade: {student['Grade']}\n")
                        slow_print(f"Math: {student['Math']}\n")
                        slow_print(f"English: {student['English']}\n")
                        slow_print(f"Science: {student['Science']}\n")
                        slow_print(f"The Average mark is: {student['Average']:.1f}\n" )
                        if student['Average'] >= 90:
                
                            student["Rating"] = "perfect"
                
                                
                            slow_print("The students grade is EXCELLENT")
                                
                        elif 80 <= student['Average'] < 90:
                
                            student["Rating"] = "very good"
                
                                
                            slow_print("The students grade is VERY GOOD")
                                
                        elif 70 <= student['Average'] < 80:
                            
                            student["Rating"] = "good"
                
                                
                            slow_print("The students grade is GOOD")
                                
                        else:
                
                            student["Rating"] = "bad"
                
                                
                            slow_print("The students grade NEEDS IMPROVEMENT")
                        slow_print("-----\n")
                        time.sleep(1)

                    trys()

            

            elif opt == "8" or opt == "show names":

                slow_print("The names of the students are:")

                for p in names:
                    slow_print(p)
                    slow_print("\n")

                trys()

            elif opt == "3" or opt == "search for student":


            
                who = slow_input("Which student do you want to look for? ")

                if who == "":

                    slow_print("You have tried to trick the system")

                    trys()

                    continue

                found = False
                for student in students:
                    if who.lower() in student["Name"].lower():
                        slow_print(f"Found:\nName: {student['Name']}\nAge: {student['Age']}\nGrade: {student['Grade']}\nMath: {student['Math']}\nEnglish: {student['English']}\nScience: {student['Science']}\nAverage: {student['Average']:.1f}")
                        found = True

                if not found:
                    slow_print("The student wasn't found")

                trys()

            elif opt == "4" or opt == "show statistics":

                for student in students:
                
                    slow_print(f"The name of the student is: {student['Name']} Average marks: {student['Average']:.1f}")

                    slow_print("\n")

                trys()

            elif opt == "5" or opt == "save students":

                slow_print("The students are being saved in a file called students")

                if os.path.exists("students.txt"):
                    stdents = open("students.txt", "a")

                    for student in students[saved:]:
                        stdents.write(f"Name: {student['Name']}\nAge: {student['Age']}\nMath: {student['Math']}\nGrade: {student['Grade']}\nEnglish: {student['English']}\nScience: {student['Science']}\nAverage: {student['Average']:.1f}\n----------------------------\n\n")


                    stdents.close()

                    saved = len(students)

                    slow_print("The students have been saved successfully")

                    trys()
                else:

                    stdents = open("students.txt", "w")

                    for student in students:
                        stdents.write(f"Name: {student['Name']}\nAge: {student['Age']}\nMath: {student['Math']}\nGrade: {student['Grade']}\nEnglish: {student['English']}\nScience: {student['Science']}\nAverage: {student['Average']:.1f}\n----------------------------\n\n")


                    stdents.close()

                    saved = len(students)

                    slow_print("The students have been saved successfully")

                    trys()
            elif opt == "6" or opt == "load students":

                if os.path.exists("students.txt"):
                
                    stdents = open("students.txt", "r")

                    content = stdents.read()

                    slow_print(content)

                    stdents.close()

                    trys()
                else:
                    slow_print("The file doesn't exist yet. Use option 5 (save students) first.")

                    trys()

            elif opt == "7" or opt == "draw results":

                size = int(slow_input("What do you want the size of the pen to be? "))
                    
                speed = int(slow_input("What do you want the speed of the turtle to be? (1-10) "))
            
                stars = {"perfect": 4, "very good": 3, "good": 2, "bad": 1}
            
                t.speed(speed)
            
                t.pensize(size)

                t.clear()

                y = 250
                for student in students:
                    t.pencolor("green")
                    t.penup()
                    t.goto(-300, y)
                    t.write(f"Name: {student['Name']}\nAge: {student['Age']}\nGrade: {student['Grade']}\nMath: {student['Math']}\nEnglish: {student['English']}\nScience: {student['Science']}\nAverage: {student['Average']:.1f}\n----------------------------\n", font=("Arial", 14, "bold"))
                    t.goto(-50, y + 30)
                    t.pendown()
                    t.pencolor("#AABB29")
                    draw_stars(stars[student["Rating"]])
                    y -= 180
                trys()

            elif opt == "9" or opt == "exit":

                slow_print("Thank you for using our program")

                slow_print("Bye!!")

                exit()

            elif opt == "10" or opt == "add one student":

                
                name = slow_input("Enter the student's name: ")

                age = int(slow_input("Enter the student's age: "))

                if age == 0 or age < 0:

                    slow_print("The students age isnt correct")

                    trys()

                    continue

                grade = int(slow_input("Enter the student's grade: "))

                math = float(slow_input("Enter the student's grade for math out of 100%: "))

                english = float(slow_input("Enter the student's grade for english out of 100%: "))

                science = float(slow_input("Enter the student's grade for science out of 100%: "))

                if math > 100 or english > 100 or science > 100 or math < 0 or english < 0 or science < 0:

                    slow_print("The marks must be between 0 and 100")

                    trys()

                    continue

                else:
            
                    Average = math + english + science
                    
            
                if Average == 0:
            
                    Average = 0
            
                else:
                        
                    Average = Average/3
                
                
                if Average >= 90:

                    rating = "perfect"

                elif 80 <= Average < 90:

                    rating = "very good"

                elif 70 <= Average < 80:

                    rating = "good"

                else:

                    rating = "bad"


                names.add(name)

                guy = {"Name": name, "Age": age, "Math": math, "English": english, "Science": science, "Grade": grade, "Average": Average, "Rating": rating}

                students.append(guy)

                file = open("students.txt", "a")

                for student in students[saved:]:

                    file.write(f"Name: {student['Name']}\nAge: {student['Age']}\nGrade: {student['Grade']}\nMath: {student['Math']}\nEnglish: {student['English']}\nScience: {student['Science']}\nAverage: {student['Average']:.1f}\n----------------------------\n\n")

                file.close()

                saved = len(students)

                slow_print("The student has been saved")

                trys()

            elif opt == "11" or opt == "show subjects":

                k = 1

                for subject in subjects:

                    slow_print(f"The number {k} is: {subject}")

                    k = k + 1

                trys()

            elif opt == "12" or opt == "show how much students are there":

                slow_print(f"There are {len(names)} students.")

                time.sleep(1)

                trys()
            elif opt == "13" or opt == "delete a student":

                ask = slow_input("Who do you want to delete: ")

                found = False

                position = 0

                for student in students:

                    if ask.lower() == student["Name"].lower():

                        found = True

                        break

                    position = position + 1

                if found:

                    slow_print("The student is being deleted")

                    students.remove(student)

                    names.discard(student["Name"])

                    if position < saved:

                        saved = saved - 1

                    slow_print("The student has been deleted successfully")

                else:

                    slow_print("The student wasnt found")

                trys()

            else:

                 slow_print("You did not enter a correct choice")

                 trys()





            


        except ValueError:
            slow_print("Something went wrong: \nplease enter a number")

            trys()
        except Exception as error:
            slow_print(f"Something went wrong: \n{error}")

            trys()