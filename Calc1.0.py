print("Welcome to the calculator app!\n")

confirm = ""
everythingWorking = ""

while everythingWorking != "yes":

    while confirm.lower() != "yes":

        yourSum = None
        yourOperator = None

        while not yourSum:
            yourSum = input("Please enter up to 5 numbers with a space between each number: ")
            if not yourSum:
                print("You haven't entered anything... please try again.")
        while not yourOperator:
            yourOperator = input("Please enter an operator: ")
            if not yourOperator:
                print("You haven't entered anything... please try again.")

        sumList = yourSum.split(" ")

        if len(sumList) < 2:
            print("You need to enter at least 2 numbers. Please try again.")
            break
        elif len(sumList) == 2:
            print(f"""You asked me to calculate \n {sumList[0]} {yourOperator} {sumList[1]}""")
        if len(sumList) == 3:
            print(f"""You asked me to calculate \n {sumList[0]} {yourOperator} {sumList[1]} {yourOperator} {sumList[2]}""")
        elif len(sumList) == 4:
            print(f"""You asked me to calculate: \n {sumList[0]} {yourOperator} {sumList[1]} {yourOperator} {sumList[2]} {yourOperator} {sumList[3]}""")
        elif len(sumList) == 5:
            print(f"""You asked me to calculate: \n {sumList[0]} {yourOperator} {sumList[1]} {yourOperator} {sumList[2]} {yourOperator} {sumList[3]} {yourOperator} {sumList[4]}""")
        elif len(sumList) > 5:
            print("Sorry - looks like you've entered too many numbers! Please try again and limit your input to 5 numbers.")

        confirm = input("... Is that right? ")
        if confirm.lower() != "yes":
            print("Okay no problem, let's start again")
        else:
            everythingWorking = "yes"

        for entry in sumList:
            if entry.isnumeric():
                if yourOperator == "*" or yourOperator == "/" or yourOperator == "+" or yourOperator == "-":
                    pass
                else:
                    print("That operator doesn't look right... Please try again!")
                    break
            else:
                print("I don't like the look of those numbers! Please try again!")
                exit()

        if everythingWorking == "yes":
            if yourOperator == "+":
                if len(sumList) == 2:
                    answer = int(sumList[0]) + int(sumList[1])
                    print("The answer is: " + str(answer))
                elif len(sumList) == 3:
                    answer = int(sumList[0]) + int(sumList[1]) + int(sumList[2])
                    print("The answer is: " + str(answer))
                elif len(sumList) == 4:
                    answer = int(sumList[0]) + int(sumList[1]) + int(sumList[2]) + int(sumList[3])
                    print("The answer is: " + str(answer))
                elif len(sumList) == 5:
                    answer = int(sumList[0]) + int(sumList[1]) + int(sumList[2]) + int(sumList[3]) + int(sumList[4])
                    print("The answer is: " + str(answer))

            elif yourOperator == "-":
                if len(sumList) == 2:
                    answer = int(sumList[0]) - int(sumList[1])
                    print("The answer is: " + str(answer))
                elif len(sumList) == 3:
                    answer = int(sumList[0]) - int(sumList[1]) - int(sumList[2])
                    print("The answer is: " + str(answer))
                elif len(sumList) == 4:
                    answer = int(sumList[0]) - int(sumList[1]) - int(sumList[2]) - int(sumList[3])
                    print("The answer is: " + str(answer))
                elif len(sumList) == 5:
                    answer = int(sumList[0]) - int(sumList[1]) - int(sumList[2]) - int(sumList[3]) - int(sumList[4])
                    print("The answer is: " + str(answer))

            elif yourOperator == "*":
                if len(sumList) == 2:
                    answer = int(sumList[0]) * int(sumList[1])
                    print("The answer is: " + str(answer))
                elif len(sumList) == 3:
                    answer = int(sumList[0]) * int(sumList[1]) * int(sumList[2])
                    print("The answer is: " + str(answer))
                elif len(sumList) == 4:
                    answer = int(sumList[0]) * int(sumList[1]) * int(sumList[2]) * int(sumList[3])
                    print("The answer is: " + str(answer))
                elif len(sumList) == 5:
                    answer = int(sumList[0]) * int(sumList[1]) * int(sumList[2]) * int(sumList[3]) * int(sumList[4])
                    print("The answer is: " + str(answer))

            elif yourOperator == "/":
                for num in range(len(sumList)):
                    if sumList[num] == "0":
                        print("Sorry you can't divide by 0! Please choose new numbers!")
                        exit()
                    else:
                        pass
                if len(sumList) == 2:
                    answer = int(sumList[0]) / int(sumList[1])
                    print("The answer is: " + str(answer))
                elif len(sumList) == 3:
                    answer = int(sumList[0]) / int(sumList[1]) / int(sumList[2])
                    print("The answer is: " + str(answer))
                elif len(sumList) == 4:
                    answer = int(sumList[0]) / int(sumList[1]) / int(sumList[2]) / int(sumList[3])
                    print("The answer is: " + str(answer))
                elif len(sumList) == 5:
                    answer = int(sumList[0]) / int(sumList[1]) / int(sumList[2]) / int(sumList[3]) / int(sumList[4])
                    print("The answer is: " + str(answer))


