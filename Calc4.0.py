import operator


ops = ["+", "-", "/", "*"]
run = ""
another_number = ""


def rules():
    print("""\nWelcome to my calculator app!\n
I can accept two numbers and one operator
No need to add any spaces!\n""")


def user_sum():
    your_sum = ""
    while your_sum == "":
        your_sum = input("Please enter your sum: ")
    return your_sum


def check_sum(user_entry):
    acceptable_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/"]
    for letter in user_entry:
        if letter in acceptable_chars:
            continue
        else:
            user_entry = "stop"
    if user_entry != "stop":
        user_entry = space_list(user)
    return user_entry


def space_list(string):
    for char in string:
        if char == "/" or char == "*" or char == "+" or char == "-":
            add_space = string.replace("/", " / ").replace("*", " * ").replace("+", " + ").replace("-", " - ")
        else:
            continue
        split_list = user_list(add_space)
        return split_list


def user_list(string):
    li = string.split(" ")
    if "" in li:
        li = "stop"
    return li


# def play_again():
#     answer = input("Would you like to do another sum?\nPlease enter 'y' for yes or 'n' for no: ")
#     return answer


def separate(full_entry, operators):
    numerate = []
    operate = []
    for item in full_entry:
        if item not in operators:
            numerate.append(item)
        else:
            operate.append(item)
    final_numerate = [int(item) for item in numerate]
    return final_numerate, operate


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
    return numbers


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


while run != "n":
    rules()
    user = user_sum()
    sum_final = check_sum(user)
    # print(sum_final)
    if sum_final != "stop":
        numList, opList = separate(sum_final, ops)
        result = calculate(numbers=numList, operators=opList)
        print(f"The result of your sum is: {result[0]}")
    # another_number = play_again()

    # confirm
    
