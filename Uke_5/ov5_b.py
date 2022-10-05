while True:
    try:
        old_temp = float(input("Old temperatur: "))
    except ValueError:
        print("Not a valid number, try again.")
        continue
    else:
        break
while True:
    try:
        new_temp = float(input("New temperatur: "))
    except ValueError:
        print("Not a valid number, try again.")
        continue
    else:
        break

temp_diff = new_temp - old_temp
print(temp_diff)