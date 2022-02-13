print("Welcome to the calculator app!\n")

yourSum = input("Please enter your sum with a space between each number or operator: ")

sumList = yourSum.split(" ")
print(sumList)

allNums = []
for entry in sumList:
    if entry.isdigit():
        placement = sumList.index(entry)
        sumList[placement] = int[placement]
        print(sumList)
#         print(placement)
#         allNums.append(entry)
# print(allNums)



# action = input("Please enter an action: ")
# secondNum = float(input("Please enter a second number: "))
#
# confirm = ""
#
# while confirm.lower() != "yes":
#     print("You asked me to calculate " + str(firstNum) + " " + action + " " + str(secondNum))
#     confirm = input("... Is that right? ")
#     if confirm.lower() != "yes":
#         print("Okay no problem, let's start again")
#         break
#
#
# if action == "+":
#     answer = firstNum + secondNum
#     print("The answer is: " + str(answer))
# elif action == "-":
#     answer = firstNum - secondNum
#     print("The answer is: " + str(answer))
# elif action == "*":
#     answer = firstNum * secondNum
#     print("The answer is: " + str(answer))
# elif action == "/":
#     answer = firstNum / secondNum
#     print("The answer is: " + str(answer))
#
#     #0
