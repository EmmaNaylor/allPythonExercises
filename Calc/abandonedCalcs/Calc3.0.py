# num1 = None
# num2 = None
# part1 = "False"
#
# while part1 is False:
#     while not num1:
#         num1 = input("Please enter a number:")
#
#     try:
#         num1 = int(num1)
#         part1 = True
#     except ValueError:
#         print("That doesn't like a number... please try again.")
#
#
#     num2 = input("Please enter another number:")

myList = ["1", "2", "3"]

new_list = list(map(lambda x: int(x), myList))
print(myList)
print(new_list)
