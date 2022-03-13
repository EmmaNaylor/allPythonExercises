print("Welcome to the calculator app!\n")

allowableChars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "+", "-", "/", "*"]
sumString = []
addSpace = []

def check_allowable(entry):
    for char in entry:
        if char in allowableChars:
            sumString.append(char)
            continue
        else:
            print("""Sorry I didn't recognise one or more of your characters...
            Please only use numbers or the following operators +, -, *, /""")
            break


def add_spaces(checkedsum):
    for char in checkedsum:
        if char == "/" or char == "*" or char == "+" or char == "-":
            new_list = yourSum.replace("/", " / ").replace("*", " * ").replace("+", " + ").replace("-", " - ")
        else:
            continue

yourSum = input("Please enter your sum: ")
if not yourSum:
    print("You haven't entered anything... please try again.")

check_allowable(yourSum)
spacedList = add_spaces(yourSum)
print(sumString)
print(spacedList)









    # Division
    # Multiplication
    # Addition
    # Subtraction
    # while not yourOperator:
    #     yourOperator = input("Please enter an operator: ")
    #     if not yourOperator:
    #         print("You haven't entered anything... please try again.")

    # sumList = yourSum.split(" ")

    # if len(sumList) < 2:
    #     print("You need to enter at least 2 numbers. Please try again.")
    #     break
    # elif len(sumList) == 2:
    #     print(f"""You asked me to calculate \n {sumList[0]} {yourOperator} {sumList[1]}""")
    # if len(sumList) == 3:
    #     print(f"""You asked me to calculate \n {sumList[0]} {yourOperator} {sumList[1]} {yourOperator} {sumList[2]}""")
    # elif len(sumList) == 4:
    #     print(f"""You asked me to calculate: \n {sumList[0]} {yourOperator} {sumList[1]} {yourOperator} {sumList[2]} {yourOperator} {sumList[3]}""")
    # elif len(sumList) == 5:
    #     print(f"""You asked me to calculate: \n {sumList[0]} {yourOperator} {sumList[1]} {yourOperator} {sumList[2]} {yourOperator} {sumList[3]} {yourOperator} {sumList[4]}""")
    # elif len(sumList) > 9:
    #     print("Sorry - looks like you've entered too many numbers! Please try again and limit your input to 5 numbers and four operators.")

    # else:
    #     everythingWorking = "yes"
    #
    # for entry in sumList:
    #     if entry in allowableChars:
    #     if yourOperator == "*" or yourOperator == "/" or yourOperator == "+" or yourOperator == "-":
    #         pass
    #     else:
    #         print("That operator doesn't look right... Please try again!")
    #         break
    # else:
    #     print("I don't like the look of those numbers! Please try again!")
    #     exit()
    #
    # if everythingWorking == "yes":
    #     if yourOperator == "+":
    #         if len(sumList) == 2:
    #             answer = int(sumList[0]) + int(sumList[1])
    #             print("The answer is: " + str(answer))
    #         elif len(sumList) == 3:
    #             answer = int(sumList[0]) + int(sumList[1]) + int(sumList[2])
    #             print("The answer is: " + str(answer))
    #         elif len(sumList) == 4:
    #             answer = int(sumList[0]) + int(sumList[1]) + int(sumList[2]) + int(sumList[3])
    #             print("The answer is: " + str(answer))
    #         elif len(sumList) == 5:
    #             answer = int(sumList[0]) + int(sumList[1]) + int(sumList[2]) + int(sumList[3]) + int(sumList[4])
    #             print("The answer is: " + str(answer))
    #
    #     elif yourOperator == "-":
    #         if len(sumList) == 2:
    #             answer = int(sumList[0]) - int(sumList[1])
    #             print("The answer is: " + str(answer))
    #         elif len(sumList) == 3:
    #             answer = int(sumList[0]) - int(sumList[1]) - int(sumList[2])
    #             print("The answer is: " + str(answer))
    #         elif len(sumList) == 4:
    #             answer = int(sumList[0]) - int(sumList[1]) - int(sumList[2]) - int(sumList[3])
    #             print("The answer is: " + str(answer))
    #         elif len(sumList) == 5:
    #             answer = int(sumList[0]) - int(sumList[1]) - int(sumList[2]) - int(sumList[3]) - int(sumList[4])
    #             print("The answer is: " + str(answer))
    #
    #     elif yourOperator == "*":
    #         if len(sumList) == 2:
    #             answer = int(sumList[0]) * int(sumList[1])
    #             print("The answer is: " + str(answer))
    #         elif len(sumList) == 3:
    #             answer = int(sumList[0]) * int(sumList[1]) * int(sumList[2])
    #             print("The answer is: " + str(answer))
    #         elif len(sumList) == 4:
    #             answer = int(sumList[0]) * int(sumList[1]) * int(sumList[2]) * int(sumList[3])
    #             print("The answer is: " + str(answer))
    #         elif len(sumList) == 5:
    #             answer = int(sumList[0]) * int(sumList[1]) * int(sumList[2]) * int(sumList[3]) * int(sumList[4])
    #             print("The answer is: " + str(answer))
    #
    #     elif yourOperator == "/":
    #         for num in range(len(sumList)):
    #             if sumList[num] == "0":
    #                 print("Sorry you can't divide by 0! Please choose new numbers!")
    #                 exit()
    #             else:
    #                 pass
    #         if len(sumList) == 2:
    #             answer = int(sumList[0]) / int(sumList[1])
    #             print("The answer is: " + str(answer))
    #         elif len(sumList) == 3:
    #             answer = int(sumList[0]) / int(sumList[1]) / int(sumList[2])
    #             print("The answer is: " + str(answer))
    #         elif len(sumList) == 4:
    #             answer = int(sumList[0]) / int(sumList[1]) / int(sumList[2]) / int(sumList[3])
    #             print("The answer is: " + str(answer))
    #         elif len(sumList) == 5:
    #             answer = int(sumList[0]) / int(sumList[1]) / int(sumList[2]) / int(sumList[3]) / int(sumList[4])
    #             print("The answer is: " + str(answer))