# yourSum = input("Please enter up to 5 numbers with a space between each number: ")
# yourOperator = input("Please enter an operator: ")
# sumList = yourSum.split(" ")

confirm = ""
while confirm.lower() != "yes":
    yourSum = input("Please enter up to 5 numbers with a space between each number: ")
    yourOperator = input("Please enter an operator: ")
    sumList = yourSum.split(" ")

    if not yourSum:
        print("You haven't entered anything... please try again.")
    if yourOperator == "*" or yourOperator == "/" or yourOperator == "+" or yourOperator == "-":
        print("Cool!")
    else:
        print("Sorry I don't recognise that operator - please try again")
        break
    if len(sumList) < 2:
        print("You need to enter at least 2 numbers. Please try again.")
    elif len(sumList) == 2:
        firstNum = sumList[0]
        secondNum = sumList[1]
        print(f"""You asked me to calculate \n {firstNum} {yourOperator} {secondNum}""")
    if len(sumList) == 3:
        firstNum = sumList[0]
        secondNum = sumList[1]
        thirdNum = sumList[2]
        print(f"""You asked me to calculate \n {firstNum} {yourOperator} {secondNum} {yourOperator} {thirdNum}""")
    elif len(sumList) == 4:
        firstNum = sumList[0]
        secondNum = sumList[1]
        thirdNum = sumList[2]
        fourthNum = sumList[3]
        print(f"""You asked me to calculate: \n {firstNum} {yourOperator} {secondNum} {yourOperator} {thirdNum} {yourOperator} {fourthNum}""")
    elif len(sumList) == 5:
        firstNum = sumList[0]
        secondNum = sumList[1]
        thirdNum = sumList[2]
        fourthNum = sumList[3]
        fifthNum = sumList[4]
        print(f"""You asked me to calculate: \n {firstNum} {yourOperator} {secondNum} {yourOperator} {thirdNum} {yourOperator} {fourthNum} {yourOperator} {fifthNum}""")




    confirm = input("... Is that right? ")
    if confirm.lower() != "yes":
        print("Okay no problem, let's start again")






# # for loop to test that all items in the list or either a digit or one of the specified operators
#
# for enum, entry in enumerate(sumList):
#     if entry.isdigit() or entry == "*" or entry == "/" or entry == "+" or entry == "-":
#         continue
#     else:
#         print("Something went wrong - please try again")
#         break
#
# op1 = 0
# if sumList[1] == "/":
#     op1 += 4
# if sumList[1] == "*":
#     op1 += 3
# if sumList[1] == "+":
#     op1 += 2
# if sumList[1] == "-":
#     op1 += 1
#
# # action = input("Please enter an action: ")
# # secondNum = float(input("Please enter a second number: "))
# op2 = 0
# if sumList[3] == "/":
#     op2 += 4
# if sumList[3] == "*":
#     op2 += 3
# if sumList[3] == "+":
#     op2 += 2
# if sumList[3] == "-":
#     op2 += 1
#
#
# # divide = 1
# # multiply = 2
# # add = 3
# # subtract = 4
#
#
# if len(sumList) < 5:
#     op1 = sumList[1]
#     firstNum = int(sumList[0])
#     secondNum = int(sumList[2])
#
# elif len(sumList) < 7:
#         op1 = sumList[1]
#         op2 = sumList[3]
#         firstNum = sumList[0]
#         secondNum = sumList[2]
#         thirdNum = sumList[4]
#     if op1 > op2:
#
#
# # elif len(sumList) < 9:
# #     op1 = sumList[1]
# #     op2 = sumList[3]
# #     op3 = sumList[5]
# #     firstNum = sumList[0]
# #     secondNum = sumList[2]
# #     thirdNum = sumList[4]
# #     fourthNum = sumList[6]
# #
# # confirm = ""
# #
# # elif len(sumList) < 10:
# #     op1 = sumList[1]
# #     op2 = sumList[3]
# #     op3 = sumList[5]
# #     op4 = sumList[7]
# #     firstNum = sumList[0]
# #     secondNum = sumList[2]
# #     thirdNum = sumList[4]
# #     fourthNum = sumList[6]
# #     fifthNum = sumList[8]
# else:
#     print("Sorry - I can only take a max input of 5 numbers. Please enter a shorter sum.")
#
#
#
# # / - +  *
#
# if len(sumList) < 5:
#     if op1 == "+":
#         answer = firstNum + secondNum
#         print("The answer is: " + str(answer))
#     elif op1 == "-":
#         answer = firstNum - secondNum
#         print("The answer is: " + str(answer))
#     elif op1 == "*":
#         answer = firstNum * secondNum
#         print("The answer is: " + str(answer))
#     elif op1 == "/":
#             if firstNum == 0 or secondNum == 0:
#                 print("Sorry - you can't divide by 0. Try another sum.")
#             else:
#                 answer = firstNum / secondNum
#                 print("The answer is: " + str(answer))
#
# elif len(sumList) < 7:
#     if op1 == "+":
#         answer = firstNum + secondNum
#         print("The answer is: " + str(answer))
#     elif op1 == "-":
#         answer = firstNum - secondNum
#         print("The answer is: " + str(answer))
#     elif op1 == "*":
#         answer = firstNum * secondNum
#         print("The answer is: " + str(answer))
#     elif op1 == "/":
#             if firstNum == 0 or secondNum == 0:
#                 print("Sorry - you can't divide by 0. Try another sum.")
#             else:
#                 answer = firstNum / secondNum
#                 print("The answer is: " + str(answer))
#
#
#
#
#
# #
# #
# # if action == "+":
# #     answer = firstNum + secondNum
# #     print("The answer is: " + str(answer))
# # elif action == "-":
# #     answer = firstNum - secondNum
# #     print("The answer is: " + str(answer))
# # elif action == "*":
# #     answer = firstNum * secondNum
# #     print("The answer is: " + str(answer))
# # elif action == "/":
# #     answer = firstNum / secondNum
# #     print("The answer is: " + str(answer))
# #
# #     #0
# #         break
