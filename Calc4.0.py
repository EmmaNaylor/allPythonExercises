import calc_module

user = ""


while user != "q":
    calc_module.rules()
    user = calc_module.user_sum()
    if user != "q":
        sum_final = calc_module.check_sum(user)
        if sum_final != "stop":
            numList, opList = calc_module.separate(sum_final)
            result = calc_module.calculate(numList, opList)
