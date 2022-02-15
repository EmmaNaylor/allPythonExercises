print("Welcome to the calculator app!\n")

yourSum = input("Please enter your sum with a space between each number or operator: ")

sumList = yourSum.split(" ")

# for loop to test that all items in the list or either a digit or one of the specified operators

for enum, entry in enumerate(sumList):
    if entry.isdigit() or entry == "*" or entry == "/" or entry == "+" or entry == "-":
        continue
    else:
        print("Something went wrong - please try again")
        break

op1 = 0
if sumList[1] == "/":
    op1 += 4
if sumList[1] == "*":
    op1 += 3
if sumList[1] == "+":
    op1 += 2
if sumList[1] == "-":
    op1 += 1

op2 = 0
if sumList[3] == "/":
    op2 += 4
if sumList[3] == "*":
    op2 += 3
if sumList[3] == "+":
    op2 += 2
if sumList[3] == "-":
    op2 += 1


# divide = 1
# multiply = 2
# add = 3
# subtract = 4


if len(sumList) < 5:
    op1 = sumList[1]
    firstNum = int(sumList[0])
    secondNum = int(sumList[2])

elif len(sumList) < 7:
        op1 = sumList[1]
        op2 = sumList[3]
        firstNum = sumList[0]
        secondNum = sumList[2]
        thirdNum = sumList[4]
    if op1 > op2:


# elif len(sumList) < 9:
#     op1 = sumList[1]
#     op2 = sumList[3]
#     op3 = sumList[5]
#     firstNum = sumList[0]
#     secondNum = sumList[2]
#     thirdNum = sumList[4]
#     fourthNum = sumList[6]
#
#
# elif len(sumList) < 10:
#     op1 = sumList[1]
#     op2 = sumList[3]
#     op3 = sumList[5]
#     op4 = sumList[7]
#     firstNum = sumList[0]
#     secondNum = sumList[2]
#     thirdNum = sumList[4]
#     fourthNum = sumList[6]
#     fifthNum = sumList[8]
else:
    print("Sorry - I can only take a max input of 5 numbers. Please enter a shorter sum.")



# / - +  *

if len(sumList) < 5:
    if op1 == "+":
        answer = firstNum + secondNum
        print("The answer is: " + str(answer))
    elif op1 == "-":
        answer = firstNum - secondNum
        print("The answer is: " + str(answer))
    elif op1 == "*":
        answer = firstNum * secondNum
        print("The answer is: " + str(answer))
    elif op1 == "/":
            if firstNum == 0 or secondNum == 0:
                print("Sorry - you can't divide by 0. Try another sum.")
            else:
                answer = firstNum / secondNum
                print("The answer is: " + str(answer))

elif len(sumList) < 7:
    if op1 == "+":
        answer = firstNum + secondNum
        print("The answer is: " + str(answer))
    elif op1 == "-":
        answer = firstNum - secondNum
        print("The answer is: " + str(answer))
    elif op1 == "*":
        answer = firstNum * secondNum
        print("The answer is: " + str(answer))
    elif op1 == "/":
            if firstNum == 0 or secondNum == 0:
                print("Sorry - you can't divide by 0. Try another sum.")
            else:
                answer = firstNum / secondNum
                print("The answer is: " + str(answer))




# confirm = ""
# while confirm.lower() != "yes":
#     print("You asked me to calculate " + str(firstNum) + " " + action + " " + str(secondNum))
#     confirm = input("... Is that right? ")
#     if confirm.lower() != "yes":
#         print("Okay no problem, let's start again")
#         break