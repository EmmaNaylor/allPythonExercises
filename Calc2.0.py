print("Welcome to the calculator app!\n")

confirm = ""
gameOver = False

while confirm.lower() != "yes":

    yourSum = None
    allowableChars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "+", "-", "/", "*"]
    sumString = []

    while not yourSum:
        yourSum = input("Please enter your sum: ")
        if not yourSum:
            print("You haven't entered anything... please try again.")

    for char in yourSum:
        if char in allowableChars:
            sumString.append(char)
            continue
        else:
            print("Sorry I didn't recognise one or more of your characters...")
            print("Please only use numbers or the following operators +, -, *, /")
            gameOver = True
            break
    if gameOver is True:
        break
    else:
        print(f"You asked me to calculate... {yourSum}")
        confirm = input("... Is that right? ")
        if confirm.lower() != "yes":
            print("Okay no problem, let's start again")
            gameOver = True
            break

if gameOver is False:
    for char in yourSum:
        if char == "/" or char == "*" or char == "+" or char == "-":
            addSpace = yourSum.replace("/", " / ").replace("*", " * ").replace("+", " + ").replace("-", " - ")
        else:
            continue

if gameOver is False:
    try:
        sumList = addSpace.split(" ")
        print(sumList)
    except NameError:
        print("Looks like you haven't entered a valid operator. Please enter a new sum")
        gameOver = True
    if sumList[-1] == "":
        sumList.pop()
    if sumList[-1] == "/" or sumList[-1] == "*" or sumList[-1] == "+" or sumList[-1] == "-":
        sumList.pop()
        print(sumList)







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