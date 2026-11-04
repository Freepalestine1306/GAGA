from slow_print import slow_print, slow_input

slow_print("Welcome to Calculator Python Edition")

while True:
    try:
        count = int(slow_input("How many numbers? "))

        if count < 1:
            slow_print("Please enter at least 1 number")
            continue

        numbers = []
        for i in range(count):
            number = float(slow_input(f"Enter number {i + 1}: "))
            numbers.append(number)

        op = slow_input("Choose an operation (+  -  *  /): ")

        if op not in ["+", "-", "*", "/"]:
            slow_print("That is not a valid operation")
        else:
            answer = numbers[0]
            for n in numbers[1:]:
                if op == "+":
                    answer = answer + n
                elif op == "-":
                    answer = answer - n
                elif op == "*":
                    answer = answer * n
                elif op == "/":
                    answer = answer / n

            slow_print(f"The answer is: {answer}")

    except ValueError:
        slow_print("That is not a valid number")
    except ZeroDivisionError:
        slow_print("You can't divide by zero")

    again = slow_input("Do you want to try again? (yes/no): ").lower()
    if again not in ["yes", "y"]:
        slow_print("Thank you for using Calculator Python Edition")
        slow_print("Goodbye!")
        break