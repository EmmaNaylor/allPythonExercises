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