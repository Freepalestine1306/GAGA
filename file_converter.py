import subprocess
from slow_print import slow_print, slow_input

while True:
    try:
        convert = slow_input("Hello user do you want to go to a file?\n")

        if convert == "yes" or convert == "Yes" or convert == "YES" or convert == "y" or convert == "Y":

        
        
            while True:
                file_name = slow_input("What is the name of the file you want to go to \nif you want calculator enter number 1 \nor turtle type 2 \nor consumer type 3 \nor info type 4 \nor loope type 5\nif you want to create a file type the name you want for the file and after that .txt:\nif you want to read a file type the name of the file and after that .read: ")

                if file_name == "1":
                    
                    subprocess.run(["python", "Homework_session4.py"])
                    break

                elif file_name == "2":

                    subprocess.run(["python", "turtle_drawing.py"])
                    break

                elif file_name == "4":

                    subprocess.run(["python", "Homework_session7.py"])
                    break

                elif file_name == "5":

                    subprocess.run(["python", "Homework_session9.py"])
                    break

                elif file_name.endswith(".read"):

                    file = open(file_name[:-5], "r")

                    content = file.read()

                    slow_print(content)

                    file.close()

                    again = slow_input("Do you want to try again? ")

                    if again.lower() != "yes" and again.lower() != "y":
                        break


                elif file_name == "3":

                    subprocess.run(["python", "Homework_session5.py"])
                    break

                elif file_name.endswith(".txt"):
                    file = open(file_name, "w")

                    text = slow_input("What is the text you want to write in the file: ")

                    file.write(text)
                    file.close()

                    again = slow_input("Do you want to try again? ")

                    if again.lower() != "yes" and again.lower() != "y":
                        break


                else:
                    slow_print("You did not enter a file name")

                    try_again = slow_input("Do you want to try again? ")

                    if try_again.lower() != "yes" and try_again.lower() != "y":
                        break

                    if again.lower() != "no" and again.lower() != "n":
                        
                         slow_print("Thanks for using file converter")

                         slow_print("Goodbye")       


                        exit()

        elif convert == "no" or convert == "No" or convert == "NO" or convert == "n" or convert == "N":
             slow_print("You did not want to go to a file")

             slow_print("Thanks for using file converter")

             slow_print("Goodbye")       

             exit()
        again = slow_input("Do you want to try again? ")

        if again.lower() != "yes" and again.lower() != "y":
            break

    except (ValueError, NameError, TypeError, IndexError, ZeroDivisionError, KeyError):
        slow_print("You entered something wrong")

        try_again = slow_input("Do you want to try again? ")

        if try_again.lower() != "yes" and try_again.lower() != "y":
            break

    except FileNotFoundError:
        slow_print("You entered a file that does not exist")

        if convert == "no" or convert == "No" or convert == "NO" or convert == "n" or convert == "N":
             slow_print("You did not want to go to a file")

             slow_print("Thanks for using file converter")

             slow_print("Goodbye")       

             exit()

