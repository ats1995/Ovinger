from sympy import true


def check_for_float(question_for_user):
    valid_value = False
    while not valid_value:
        try:
            value_str = input(question_for_user)
            value_float = float(value_str)
            valid_value = True
        except ValueError:
            print("Invalid float input.")
    return value_float


newTemp = check_for_float("New temperatur: ")
oldTemp = check_for_float("Old temperatur: ")
tempDiff = newTemp - oldTemp
print(tempDiff)