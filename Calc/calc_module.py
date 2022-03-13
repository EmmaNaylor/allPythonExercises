import operator


# prints rules
def rules():
    print("""\nWelcome to my calculator app!
I can accept up to four numbers and 3 operators
No need to add any spaces!
Please enter your sum - or enter 'q' to quit.\n""")


# takes input from user (sum) and returns
def user_sum():
    your_sum = ""
    while your_sum == "":
        your_sum = input("Please enter your sum: ")
        if your_sum == "q":
            print("Okay I'll quit it! Come back soon :) ")
    return your_sum


# runs several checks to make sure user entry is acceptable
def check_sum(user_entry):
    acceptable_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/"]
    for letter in user_entry:
        if letter in acceptable_chars:
            continue
        else:
            user_entry = "stop"
    if "/" not in user_entry and "*" not in user_entry and "+" not in user_entry and "-" not in user_entry:
        user_entry = "stop"
        print("You've entered an incalculable sum. Please try again.")
    if user_entry != "stop":
        user_entry = space_list(user_entry)
    return user_entry


# replaces operators in sum with a spaced version of itself - allowing for the list to be split using the spaces created
def space_list(string):
    for char in string:
        if char == "/" or char == "*" or char == "+" or char == "-":
            add_space = string.replace("/", " / ").replace("*", " * ").replace("+", " + ").replace("-", " - ")
        else:
            continue
        split_list = user_list(add_space)
        if split_list == "stop":
            print("You've entered an incalculable sum. Please try again.")
        return split_list


# splits entry into list
def user_list(string):
    li = string.split(" ")
    if "" in li:
        li = "stop"
    return li


# separates the numbers and the operators into two different lists
def separate(full_entry):
    ops = ["+", "-", "/", "*"]
    numerate = []
    operate = []
    for item in full_entry:
        if item not in ops:
            numerate.append(item)
        else:
            operate.append(item)
    final_numerate = [int(item) for item in numerate]
    return final_numerate, operate


# runs the calculation until all operators used - prioritisation in order of BIDMAS
def calculate(numbers, operators):
    while len(operators) != 0:
        for index, item in enumerate(operators):
            if item == "/":
                numbers = divide(index, numbers)
                operators.pop(index)
            elif item == "*" and "/" not in operators:
                numbers = multiply(index, numbers)
                operators.pop(index)
            elif item == "+" and "/" not in operators and "*" not in operators:
                numbers = add(index, numbers)
                operators.pop(index)
            elif item == "-" and "/" not in operators and "*" not in operators and "+" not in operators:
                numbers = subtract(index, numbers)
                operators.pop(index)
    print(f"The result of your sum is: {numbers[0]}")
    return numbers


# applies division to two numbers based on position of operator in the list
def divide(position, nums):
    answer = []
    if len(nums) == 2:
        one, two = nums
        simple_sum = operator.truediv(one, two)
        answer.append(simple_sum)
        return answer
    elif len(nums) == 3:
        if position == 0:
            sum_1 = operator.truediv(nums[0], nums[1])
            left_over = nums[2]
            answer.extend([sum_1, left_over])
        else:
            sum_1 = operator.truediv(nums[1], nums[2])
            left_over = nums[0]
            answer.extend([left_over, sum_1])
    elif len(nums) == 4:
        if position == 0:
            sum_1 = operator.truediv(nums[0], nums[1])
            left_over_1 = nums[2]
            left_over_2 = nums[3]
            answer.extend([sum_1, left_over_1, left_over_2])
        elif position == 1:
            sum_1 = operator.truediv(nums[1], nums[2])
            left_over_1 = nums[0]
            left_over_2 = nums[4]
            answer.extend([left_over_1, sum_1, left_over_2])
        else:
            sum_1 = operator.truediv(nums[2], nums[3])
            left_over_1 = nums[0]
            left_over_2 = nums[1]
            answer.extend([left_over_1, left_over_2, sum_1])
    return answer


# applies multiplication to two numbers based on position of operator in the list
def multiply(position, nums):
    answer = []
    if len(nums) == 2:
        one, two = nums
        simple_sum = operator.mul(one, two)
        answer.append(simple_sum)
        return answer
    elif len(nums) == 3:
        if position == 0:
            sum_1 = operator.mul(nums[0], nums[1])
            left_over = nums[2]
            answer.extend([sum_1, left_over])
        else:
            sum_1 = operator.mul(nums[1], nums[2])
            left_over = nums[0]
            answer.extend([left_over, sum_1])
    elif len(nums) == 4:
        if position == 0:
            sum_1 = operator.mul(nums[0], nums[1])
            left_over_1 = nums[2]
            left_over_2 = nums[3]
            answer.extend([sum_1, left_over_1, left_over_2])
        elif position == 1:
            sum_1 = operator.mul(nums[1], nums[2])
            left_over_1 = nums[0]
            left_over_2 = nums[4]
            answer.extend([left_over_1, sum_1, left_over_2])
        else:
            sum_1 = operator.mul(nums[2], nums[3])
            left_over_1 = nums[0]
            left_over_2 = nums[1]
            answer.extend([left_over_1, left_over_2, sum_1])
    return answer


# applies addition to two numbers based on position of operator in the list
def add(position, nums):
    answer = []
    if len(nums) == 2:
        one, two = nums
        simple_sum = operator.add(one, two)
        answer.append(simple_sum)
        return answer
    elif len(nums) == 3:
        if position == 0:
            sum_1 = operator.add(nums[0], nums[1])
            left_over = nums[2]
            answer.extend([sum_1, left_over])
        else:
            sum_1 = operator.add(nums[1], nums[2])
            left_over = nums[0]
            answer.extend([left_over, sum_1])
    elif len(nums) == 4:
        if position == 0:
            sum_1 = operator.add(nums[0], nums[1])
            left_over_1 = nums[2]
            left_over_2 = nums[3]
            answer.extend([sum_1, left_over_1, left_over_2])
        elif position == 1:
            sum_1 = operator.add(nums[1], nums[2])
            left_over_1 = nums[0]
            left_over_2 = nums[4]
            answer.extend([left_over_1, sum_1, left_over_2])
        else:
            sum_1 = operator.add(nums[2], nums[3])
            left_over_1 = nums[0]
            left_over_2 = nums[1]
            answer.extend([left_over_1, left_over_2, sum_1])
    return answer


# applies subtraction to two numbers based on position of operator in the list
def subtract(position, nums):
    answer = []
    if len(nums) == 2:
        one, two = nums
        simple_sum = operator.sub(one, two)
        answer.append(simple_sum)
        return answer
    elif len(nums) == 3:
        if position == 0:
            sum_1 = operator.sub(nums[0], nums[1])
            left_over = nums[2]
            answer.extend([sum_1, left_over])
        else:
            sum_1 = operator.sub(nums[1], nums[2])
            left_over = nums[0]
            answer.extend([left_over, sum_1])
    elif len(nums) == 4:
        if position == 0:
            sum_1 = operator.sub(nums[0], nums[1])
            left_over_1 = nums[2]
            left_over_2 = nums[3]
            answer.extend([sum_1, left_over_1, left_over_2])
        elif position == 1:
            sum_1 = operator.sub(nums[1], nums[2])
            left_over_1 = nums[0]
            left_over_2 = nums[4]
            answer.extend([left_over_1, sum_1, left_over_2])
        else:
            sum_1 = operator.sub(nums[2], nums[3])
            left_over_1 = nums[0]
            left_over_2 = nums[1]
            answer.extend([left_over_1, left_over_2, sum_1])
    return answer
